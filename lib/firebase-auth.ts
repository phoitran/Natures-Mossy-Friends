import { env } from 'cloudflare:workers';
import { cookies } from 'next/headers';
import { standaloneAuth } from './auth-mode';

const ID_COOKIE = '__Host-mossy-id';
const REFRESH_COOKIE = '__Host-mossy-refresh';
const cookieOptions = { httpOnly: true, secure: true, sameSite: 'lax' as const, path: '/' };
export class AuthError extends Error {
  constructor(public code: string, public status = 400) { super(code); }
}
export function firebaseReady() { return standaloneAuth && Boolean(env.FIREBASE_API_KEY && env.FIREBASE_PROJECT_ID); }
function key() {
  if (!firebaseReady()) throw new AuthError('NOT_CONFIGURED', 503);
  return encodeURIComponent(env.FIREBASE_API_KEY!);
}
async function provider(url: string, body: string, contentType = 'application/json') {
  let response: Response;
  try { response = await fetch(url, { method: 'POST', headers: { 'Content-Type': contentType }, body, signal: AbortSignal.timeout(10000) }); }
  catch { throw new AuthError('UNAVAILABLE', 503); }
  let data;
  try { data = await response.json() as any; } catch { throw new AuthError('UNAVAILABLE', 503); }
  if (!response.ok) throw new AuthError(String(data.error?.message || 'UNAVAILABLE').split(' : ')[0], response.status >= 500 ? 503 : 400);
  return data;
}
export function firebaseRequest(method: string, body: unknown) {
  return provider(`https://identitytoolkit.googleapis.com/v1/accounts:${method}?key=${key()}`, JSON.stringify(body));
}
export async function clearFirebaseSession() {
  const jar = await cookies();
  for (const name of [ID_COOKIE, REFRESH_COOKIE]) jar.set(name, '', { ...cookieOptions, maxAge: 0 });
}
export async function saveFirebaseSession(data: { idToken: string; refreshToken: string }) {
  if (!data.idToken || !data.refreshToken) throw new AuthError('UNAVAILABLE', 503);
  const jar = await cookies();
  jar.set(ID_COOKIE, data.idToken, { ...cookieOptions, maxAge: 3600 });
  jar.set(REFRESH_COOKIE, data.refreshToken, { ...cookieOptions, maxAge: 60 * 60 * 24 * 14 });
}
function tokenClaims(token: string) {
  try { return JSON.parse(atob(token.split('.')[1].replace(/-/g, '+').replace(/_/g, '/'))) as Record<string, any>; }
  catch { throw new AuthError('INVALID_ID_TOKEN'); }
}
export async function lookupFirebaseToken(idToken: string) {
  // Google verifies the token. Decoded claims are only used after that verification.
  const data = await firebaseRequest('lookup', { idToken });
  const user = data.users?.[0];
  const claims = tokenClaims(idToken);
  if (!user?.localId || !user.email || user.disabled || claims.sub !== user.localId ||
      claims.aud !== env.FIREBASE_PROJECT_ID || claims.iss !== `https://securetoken.google.com/${env.FIREBASE_PROJECT_ID}`) {
    throw new AuthError('INVALID_ID_TOKEN');
  }
  return { userId: `firebase_${user.localId}`, email: user.email as string, displayName: user.email as string,
    fullName: null, emailVerified: user.emailVerified === true, idToken, authenticatedAt: Number(claims.auth_time || 0) };
}
export async function firebaseSession() {
  if (!firebaseReady()) return null;
  const jar = await cookies();
  const idToken = jar.get(ID_COOKIE)?.value;
  if (idToken) {
    try { return await lookupFirebaseToken(idToken); }
    catch (error) {
      if (!(error instanceof AuthError) || error.status === 503) throw error;
      if (!['TOKEN_EXPIRED', 'INVALID_ID_TOKEN'].includes(error.code)) { await clearFirebaseSession(); return null; }
    }
  }
  const refreshToken = jar.get(REFRESH_COOKIE)?.value;
  if (!refreshToken) return null;
  try {
    const data = await provider(`https://securetoken.googleapis.com/v1/token?key=${key()}`,
      new URLSearchParams({ grant_type: 'refresh_token', refresh_token: refreshToken }).toString(), 'application/x-www-form-urlencoded');
    const user = await lookupFirebaseToken(data.id_token);
    await saveFirebaseSession({ idToken: data.id_token, refreshToken: data.refresh_token });
    return user;
  } catch (error) {
    if (!(error instanceof AuthError) || error.status === 503) throw error;
    await clearFirebaseSession();
    return null;
  }
}
export function authErrorResponse(error: unknown) {
  let message = 'Sign-in is temporarily unavailable. Please try again.';
  let status = error instanceof AuthError ? error.status : 503;
  if (error instanceof AuthError) {
    if (['INVALID_LOGIN_CREDENTIALS', 'INVALID_PASSWORD', 'EMAIL_NOT_FOUND', 'USER_DISABLED'].includes(error.code)) message = 'Check your email and password, or reset your password.';
    if (error.code === 'EMAIL_EXISTS') message = 'Try signing in or resetting your password for this email.';
    if (error.code.startsWith('WEAK_PASSWORD') || error.code === 'PASSWORD_DOES_NOT_MEET_REQUIREMENTS') message = 'Choose a stronger password with at least 12 characters.';
    if (error.code === 'INVALID_EMAIL') message = 'Enter a valid email address.';
    if (['TOO_MANY_ATTEMPTS_TRY_LATER', 'RATE_LIMITED'].includes(error.code)) { message = 'Too many attempts. Please try again in 15 minutes.'; status = 429; }
    if (error.code === 'NOT_CONFIGURED') message = 'Email signup is not ready yet. You can keep exploring as a guest.';
    if (error.code === 'CREDENTIAL_TOO_OLD_LOGIN_AGAIN') { message = 'Sign out and sign in again before deleting your account.'; status = 401; }
  }
  return Response.json({ error: message }, { status, headers: { 'Cache-Control': 'no-store' } });
}
