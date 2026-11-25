import { env } from 'cloudflare:workers';
import { standaloneAuth } from '../../../lib/auth-mode';
import { AuthError, authErrorResponse, clearFirebaseSession, firebaseReady, firebaseRequest, firebaseSession, lookupFirebaseToken, saveFirebaseSession } from '../../../lib/firebase-auth';
import { db, fail, jsonBody, reply, sameOrigin } from '../../../lib/server-data';

async function throttle(req: Request, email: string, action: string) {
  const now = Math.floor(Date.now() / 1000), window = Math.floor(now / 900);
  const ip = req.headers.get('cf-connecting-ip') || 'local';
  await db().prepare('DELETE FROM auth_attempts WHERE expires_at < ?').bind(now).run();
  for (const [value, limit] of [[`ip:${ip}`, 30], [`email:${email}:${action}`, 6]] as const) {
    const hash = Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(value)))).map(n => n.toString(16).padStart(2, '0')).join('');
    const row = await db().prepare('INSERT INTO auth_attempts(id,attempts,expires_at) VALUES(?,1,?) ON CONFLICT(id) DO UPDATE SET attempts=attempts+1 RETURNING attempts').bind(`${window}:${hash}`, (window + 1) * 900).first<{ attempts: number }>();
    if (!row || row.attempts > limit) throw new AuthError('RATE_LIMITED', 429);
  }
}

export async function POST(req: Request) {
  if (!sameOrigin(req)) return fail('Request origin is not allowed.', 403);
  if (!standaloneAuth) return fail('Use the sign-in option on this site.', 404);
  try {
    const body = await jsonBody(req);
    if (!body || typeof body !== 'object' || Array.isArray(body)) return fail('Enter valid sign-in details.');
    if (body.action === 'signout') { await clearFirebaseSession(); return reply({ ok: true }); }
    if (!firebaseReady()) throw new AuthError('NOT_CONFIGURED', 503);
    if (!['signup', 'signin', 'reset', 'resend'].includes(body.action)) return fail('Choose a valid sign-in action.');
    if (body.action === 'resend') {
      const session = await firebaseSession();
      if (!session) return fail('Sign in to resend your verification email.', 401);
      if (session.emailVerified) return reply({ ok: true });
      await throttle(req, session.email.toLowerCase(), body.action);
      await firebaseRequest('sendOobCode', { requestType: 'VERIFY_EMAIL', idToken: session.idToken });
      return reply({ ok: true });
    }
    const email = typeof body.email === 'string' ? body.email.trim() : '';
    if (email.length > 254 || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return fail('Enter a valid email address.');
    if (body.action === 'signup' && (body.adult !== true || body.policy !== true)) return fail('Confirm you are an adult and acknowledge the Privacy Policy.');
    if (!env.PRIVACY_CONTACT_EMAIL) return fail('Account registration is not ready yet.', 423);
    if (body.action !== 'reset' && (typeof body.password !== 'string' || body.password.length > 256 || body.password.length < (body.action === 'signup' ? 12 : 1))) return fail('Use a password between 12 and 256 characters for a new account.');
    await throttle(req, email.toLowerCase(), body.action);
    if (body.action === 'reset') {
      try { await firebaseRequest('sendOobCode', { requestType: 'PASSWORD_RESET', email }); }
      catch (error) { if (!(error instanceof AuthError) || !['EMAIL_NOT_FOUND', 'INVALID_LOGIN_CREDENTIALS'].includes(error.code)) throw error; }
      return reply({ ok: true, message: 'If this email has an account, a password-reset email is on its way.' });
    }
    const data = await firebaseRequest(body.action === 'signup' ? 'signUp' : 'signInWithPassword', { email, password: body.password, returnSecureToken: true });
    const user = await lookupFirebaseToken(data.idToken);
    await saveFirebaseSession(data);
    let verificationSent = false;
    if (body.action === 'signup') {
      try { await firebaseRequest('sendOobCode', { requestType: 'VERIFY_EMAIL', idToken: data.idToken }); verificationSent = true; }
      catch { /* The account exists; the verification screen offers a truthful retry. */ }
    }
    return reply({ ok: true, verified: user.emailVerified, verificationSent });
  } catch (error) { return authErrorResponse(error); }
}
