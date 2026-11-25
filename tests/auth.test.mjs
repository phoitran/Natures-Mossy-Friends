import { build } from 'esbuild';
import { DatabaseSync } from 'node:sqlite';
import { mkdirSync, readdirSync, readFileSync } from 'node:fs';
import assert from 'node:assert/strict';

const sql = new DatabaseSync(':memory:');
for (const file of readdirSync('drizzle').filter(f => f.endsWith('.sql')).sort()) sql.exec(readFileSync('drizzle/' + file, 'utf8').replaceAll('--> statement-breakpoint', ''));
const DB = { prepare(query) { let params = []; const s = { bind(...p) { params = p; return s; }, async first() { return sql.prepare(query).get(...params) || null; }, async all() { return { results: sql.prepare(query).all(...params) }; }, async run() { return { meta: { changes: Number(sql.prepare(query).run(...params).changes) } }; } }; return s; }, async batch(statements) { return Promise.all(statements.map(s => s.run())); } };
globalThis.__authEnv = { DB, PRIVACY_CONTACT_EMAIL: 'hello@example.invalid', BUCKET: { async delete() {}, async get() { return { body: 'private-test-photo' }; } } };
const jar = new Map(), cookieWrites = [];
globalThis.__authCookies = { get(name) { return jar.has(name) ? { value: jar.get(name) } : undefined; }, set(name, value, options) { cookieWrites.push({ name, value, options }); if (options.maxAge === 0) jar.delete(name); else jar.set(name, value); } };
mkdirSync('outputs/auth-tests', { recursive: true });
for (const name of ['auth', 'account', 'projects', 'photos']) await build({ entryPoints: [`app/api/${name}/route.ts`], outfile: `outputs/auth-tests/${name}.mjs`, bundle: true, platform: 'node', format: 'esm', define: { __MOSSY_STANDALONE__: 'true' }, plugins: [{ name: 'bindings', setup(b) {
  b.onResolve({ filter: /^(cloudflare:workers|next\/headers)$/ }, a => ({ path: a.path, namespace: 'test' }));
  b.onLoad({ filter: /.*/, namespace: 'test' }, a => ({ contents: a.path === 'cloudflare:workers' ? 'export const env=globalThis.__authEnv;' : 'export async function cookies(){return globalThis.__authCookies;} export async function headers(){throw new Error("Never trust Sites headers on an independent host");}', loader: 'js' }));
} }] });
const routes = {};
for (const name of ['auth', 'account', 'projects', 'photos']) routes[name] = await import(`../outputs/auth-tests/${name}.mjs`);
let checks = 0, providerCalls = 0, mailCalls = 0, outage = false, verifyFailure = false;
const users = new Map();
const token = (uid, extra = {}) => `header.${Buffer.from(JSON.stringify({ sub: uid, aud: 'mossy-test', iss: 'https://securetoken.google.com/mossy-test', auth_time: Math.floor(Date.now() / 1000), ...extra })).toString('base64url')}.signature`;
const claims = t => JSON.parse(Buffer.from(t.split('.')[1], 'base64url').toString());
const response = (data, status = 200) => Response.json(data, { status });
globalThis.fetch = async (url, options) => {
  providerCalls++;
  if (outage) return response({ error: { message: 'UNAVAILABLE' } }, 503);
  assert.match(url, /^https:\/\/(identitytoolkit|securetoken)\.googleapis\.com\//);
  if (url.includes('securetoken')) {
    const uid = new URLSearchParams(options.body).get('refresh_token').replace('refresh-', '');
    if (!users.has(uid)) return response({ error: { message: 'INVALID_REFRESH_TOKEN' } }, 400);
    return response({ id_token: token(uid), refresh_token: `refresh-${uid}` });
  }
  const body = JSON.parse(options.body), method = new URL(url).pathname.split(':')[1];
  if (method === 'signUp') {
    const uid = `user${users.size + 1}`; users.set(uid, { localId: uid, email: body.email, emailVerified: false });
    return response({ idToken: token(uid), refreshToken: `refresh-${uid}` });
  }
  if (method === 'signInWithPassword') {
    const user = [...users.values()].find(u => u.email === body.email);
    if (!user || body.password !== 'a long test password') return response({ error: { message: 'INVALID_LOGIN_CREDENTIALS' } }, 400);
    return response({ idToken: token(user.localId), refreshToken: `refresh-${user.localId}` });
  }
  if (method === 'lookup') {
    if (body.idToken === 'expired') return response({ error: { message: 'TOKEN_EXPIRED' } }, 400);
    let decoded; try { decoded = claims(body.idToken); } catch { return response({ error: { message: 'INVALID_ID_TOKEN' } }, 400); }
    const user = users.get(decoded.sub);
    return user ? response({ users: [user] }) : response({ error: { message: 'USER_NOT_FOUND' } }, 400);
  }
  if (method === 'sendOobCode') {
    if (verifyFailure && body.requestType === 'VERIFY_EMAIL') return response({ error: { message: 'UNAVAILABLE' } }, 503);
    if (body.email === 'missing@example.invalid') return response({ error: { message: 'EMAIL_NOT_FOUND' } }, 400);
    mailCalls++; return response({ email: body.email || 'test@example.invalid' });
  }
  if (method === 'delete') { users.delete(claims(body.idToken).sub); return response({}); }
  throw new Error(`Unexpected provider method ${method}`);
};
async function call(route, method = 'GET', body, options = {}) {
  const req = new Request(`https://mossy.test/api/${route}${options.search || ''}`, { method, headers: { origin: options.origin || 'https://mossy.test', 'content-type': 'application/json', 'cf-connecting-ip': '192.0.2.1', 'oai-authenticated-user-id': 'legacy-owner', 'oai-authenticated-user-email': 'adult@example.invalid' }, body: body === undefined ? undefined : JSON.stringify(body) });
  const r = await routes[route][method](req);
  return { status: r.status, data: r.headers.get('content-type')?.includes('json') ? await r.json() : await r.text(), headers: r.headers };
}
function eq(a, b, label) { assert.deepEqual(a, b, label); checks++; }
const signup = { action: 'signup', email: 'adult@example.invalid', password: 'a long test password', adult: true, policy: true };
eq((await call('account')).data.user, null, 'unconfigured standalone ignores forged platform headers');
eq((await call('account')).data.authReady, false, 'unconfigured signup is visibly unavailable');
eq((await call('projects')).status, 401, 'no platform-header fallback for private data');
eq((await call('auth', 'POST', signup)).status, 503, 'unconfigured signup fails closed');
eq(providerCalls, 0, 'missing configuration makes no provider request');
Object.assign(globalThis.__authEnv, { FIREBASE_API_KEY: 'test-key', FIREBASE_PROJECT_ID: 'mossy-test' });
eq((await call('auth', 'POST', signup, { origin: 'https://evil.test' })).status, 403, 'cross-origin auth rejected');
eq((await call('auth', 'POST', { ...signup, adult: false })).status, 400, 'adult confirmation before creating identity');
eq((await call('auth', 'POST', { ...signup, password: 'short' })).status, 400, 'password length enforced server-side');
eq((await call('auth', 'POST', { ...signup, email: 'wrong' })).status, 400, 'email validated');
let r = await call('auth', 'POST', signup);
eq(r.status, 200, 'signup creates identity'); eq(r.data.verificationSent, true, 'signup sends verification email');
eq(Object.keys(r.data).sort(), ['ok', 'verificationSent', 'verified'], 'no tokens or password returned to browser scripts');
eq(cookieWrites.every(c => c.options.secure && c.options.httpOnly && c.options.sameSite === 'lax' && c.options.path === '/'), true, 'sessions use secure HttpOnly host cookies');
eq((await call('account')).data.user.emailVerified, false, 'unverified user sees verification screen');
eq((await call('account', 'POST', { adult: true, policy: true })).status, 401, 'unverified email cannot create profile');
eq((await call('projects')).status, 401, 'unverified email cannot read projects');
eq((await call('auth', 'POST', { action: 'resend' })).status, 200, 'verification can be resent');
users.get('user1').emailVerified = true;
eq((await call('account')).data.user.emailVerified, true, 'verification completion is read from provider');
sql.prepare('INSERT INTO accounts(id,email,name,policy_version,created_at) VALUES(?,?,?,?,?)').run('legacy-owner', signup.email, '', 'legacy', '2026-11-22');
eq((await call('account')).data.account, false, 'matching legacy email does not automatically claim account');
eq((await call('account', 'POST', { adult: true, policy: true })).status, 200, 'verified adult can create profile');
eq(sql.prepare('SELECT COUNT(*) AS n FROM accounts').get().n, 2, 'legacy account remains separate');
const project = { id: 'new-project', activityId: 'SPR-01', variant: 'young', step: 0, status: 'in-progress' };
eq((await call('projects', 'POST', project)).status, 200, 'verified account saves a project');
eq(sql.prepare('SELECT owner_id FROM projects').get().owner_id, 'firebase_user1', 'ownership comes from verified provider identity');
sql.prepare('INSERT INTO photos(id,owner_id,project_id,object_key,bytes,mime,created_at) VALUES(?,?,?,?,?,?,?)').run('photo1', 'firebase_user1', project.id, 'photo1', 18, 'image/jpeg', '2026-11-22');
eq((await call('photos', 'GET', undefined, { search: '?id=photo1' })).status, 200, 'cookie session authorizes private image requests');
jar.set('__Host-mossy-id', 'expired');
eq((await call('account')).data.account, true, 'expired token refreshes using secure refresh cookie');
eq(jar.get('__Host-mossy-id').startsWith('header.'), true, 'refresh replaces expired token');
jar.set('__Host-mossy-id', token('user1', { aud: 'another-project' })); jar.delete('__Host-mossy-refresh');
eq((await call('account')).data.user, null, 'wrong Firebase project rejected');
await call('auth', 'POST', { action: 'signin', email: signup.email, password: signup.password });
outage = true;
eq((await call('account')).status, 503, 'provider outage is reported, not silently treated as signed out');
outage = false;
jar.set('__Host-mossy-id', token('user1', { auth_time: Math.floor(Date.now() / 1000) - 600 }));
eq((await call('account', 'DELETE')).status, 401, 'old login must reauthenticate before deletion');
eq(sql.prepare('SELECT COUNT(*) AS n FROM projects').get().n, 1, 'failed recent-login check preserves data');
await call('auth', 'POST', { action: 'signout' });
eq(jar.size, 0, 'signout clears both cookies');
eq((await call('projects')).status, 401, 'signed-out private data is inaccessible');
eq((await call('auth', 'POST', { action: 'signin', email: signup.email, password: 'wrong' })).status, 400, 'incorrect password rejected');
eq((await call('auth', 'POST', { action: 'reset', email: 'missing@example.invalid' })).data.message, (await call('auth', 'POST', { action: 'reset', email: signup.email })).data.message, 'password reset does not disclose whether email exists');
verifyFailure = true;
r = await call('auth', 'POST', { ...signup, email: 'second@example.invalid' });
eq(r.status, 200, 'verification delivery failure retains recoverable new account');
eq(r.data.verificationSent, false, 'does not falsely claim verification email sent');
verifyFailure = false; users.get('user2').emailVerified = true;
await call('account', 'POST', { adult: true, policy: true });
eq((await call('projects')).data.projects.length, 0, 'second account cannot read first account projects');
eq((await call('photos', 'GET', undefined, { search: '?id=photo1' })).status, 404, 'second account cannot read first account photo');
eq((await call('projects', 'POST', project)).status, 404, 'second account cannot overwrite first account project');
sql.prepare('DELETE FROM auth_attempts').run();
for (let i = 0; i < 6; i++) await call('auth', 'POST', { action: 'reset', email: signup.email });
const sent = mailCalls;
eq((await call('auth', 'POST', { action: 'reset', email: signup.email })).status, 429, 'email requests rate limited');
eq(mailCalls, sent, 'throttle prevents provider email request');
eq(sql.prepare('SELECT id FROM auth_attempts').all().every(row => !row.id.includes('@') && !row.id.includes('192.0.2.1')), true, 'throttle stores no raw email or IP');
sql.prepare('DELETE FROM auth_attempts').run();
await call('auth', 'POST', { action: 'signin', email: signup.email, password: signup.password });
eq((await call('account', 'DELETE')).status, 200, 'recently signed-in account deletes app data and provider identity');
eq(users.has('user1'), false, 'Firebase identity deleted');
eq(jar.size, 0, 'account deletion clears session');
eq(sql.prepare('SELECT COUNT(*) AS n FROM projects').get().n, 0, 'deleted owner projects removed');
eq(sql.prepare('SELECT COUNT(*) AS n FROM accounts WHERE id=?').get('legacy-owner').n, 1, 'legacy account preserved during deletion');
console.log(`Passed ${checks} independent-auth checks.`);
