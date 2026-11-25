import { db, fail, jsonBody, reply, sameOrigin } from '../../../lib/server-data';

const kinds = ['An activity idea', 'A change I’d like', 'Something isn’t working', 'Other feedback'];
export async function POST(req: Request) {
  if (!sameOrigin(req)) return fail('Request origin is not allowed.', 403);
  try {
    const data = await jsonBody(req);
    if (!data || typeof data !== 'object' || !kinds.includes(data.kind)) return fail('Choose a feedback category.');
    if (data.website) return reply({ ok: true, deliver: false });
    const message = typeof data.message === 'string' ? data.message.trim() : '';
    const email = typeof data.email === 'string' ? data.email.trim() : '';
    if (!message || message.length > 2000) return fail('Write a message of up to 2,000 characters.');
    if (email && (email.length > 254 || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email))) return fail('Check your optional reply email.');
    const page = typeof data.page === 'string' && /^\/[a-zA-Z0-9_/-]{0,160}$/.test(data.page) ? data.page : '/';
    const activity = typeof data.activity === 'string' ? data.activity.slice(0,150).replace(/[\r\n]/g,' ') : '';
    const now = Math.floor(Date.now() / 1000), window = Math.floor(now / 900);
    const fingerprint = Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(req.headers.get('cf-connecting-ip') || 'local')))).map(n => n.toString(16).padStart(2,'0')).join('');
    await db().prepare('DELETE FROM auth_attempts WHERE expires_at < ?').bind(now).run();
    const row = await db().prepare('INSERT INTO auth_attempts(id,attempts,expires_at) VALUES(?,1,?) ON CONFLICT(id) DO UPDATE SET attempts=attempts+1 RETURNING attempts').bind(`feedback:${window}:${fingerprint}`, (window+1)*900).first<{attempts:number}>();
    if (!row || row.attempts > 3) return fail('You’ve sent a few messages recently. Please try again in 15 minutes.',429);
    return reply({ ok: true, deliver: true });
  } catch { return fail('We couldn’t send your feedback just now. Please try again.',503); }
}
