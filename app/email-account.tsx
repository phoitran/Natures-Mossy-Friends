'use client';
import { useEffect, useState } from 'react';

async function request(path: string, body?: unknown) {
  const response = await fetch(path, body ? { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) } : undefined);
  const result: any = await response.json();
  if (!response.ok) throw new Error(result.error || 'Please try again.');
  return result;
}
export default function EmailAccount({ initialAccount, onReady }: { initialAccount: any; onReady: () => Promise<void> }) {
  const [account, setAccount] = useState(initialAccount);
  const [mode, setMode] = useState<'signup' | 'signin' | 'reset'>('signup');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState('');
  const [message, setMessage] = useState('');
  useEffect(() => { setAccount(initialAccount); }, [initialAccount]);
  async function run(action: () => Promise<void>) {
    setBusy(true); setError(''); setMessage('');
    try { await action(); } catch (e) { setError(e instanceof Error ? e.message : 'Please try again.'); }
    finally { setBusy(false); }
  }
  async function refresh() {
    const data = await request('/api/account'); setAccount(data);
    if (data.account) await onReady();
    else if (data.user && !data.user.emailVerified) setMessage('Open the verification link in your email, then check again here.');
  }
  return <div className="email-account">
    {!account ? <button className="button outline full" disabled={busy} onClick={() => run(refresh)}>Load email signup</button> : !account.authReady ? <p role="status">Email signup is being set up. You can keep exploring as a guest.</p> : account.user ? <>
      <div className="signin-identity"><span className="small">Signed in as</span><strong>{account.user.email}</strong></div>
      {!account.user.emailVerified ? <>
        <h3>Check your email</h3><p>Use the verification link to confirm this email belongs to you. Then come back to finish your account.</p>
        <button className="button primary full" disabled={busy} onClick={() => run(refresh)}>I’ve verified my email</button>
        <button className="text-button" disabled={busy} onClick={() => run(async () => { await request('/api/auth', { action: 'resend' }); setMessage('Verification email sent. Check your inbox and spam folder.'); })}>Resend verification email</button>
      </> : <form onSubmit={e => { e.preventDefault(); const form = new FormData(e.currentTarget); run(async () => {
        await request('/api/account', { name: form.get('name'), adult: form.get('adult') === 'on', policy: form.get('policy') === 'on' }); await onReady();
      }); }}>
        <label className="form-label">Your name (optional)<input name="name" maxLength={100} autoComplete="given-name" /></label>
        <label className="check-label"><input name="adult" type="checkbox" required />I am an adult creating an account for myself.</label>
        <label className="check-label"><input name="policy" type="checkbox" required />I acknowledge the Privacy Policy.</label>
        <button className="button primary full" disabled={busy}>Finish my free account</button>
      </form>}
      <button className="text-button" disabled={busy} onClick={() => run(async () => { await request('/api/auth', { action: 'signout' }); setAccount(await request('/api/account')); })}>Use a different email</button>
    </> : <>
      <h3>{mode === 'signup' ? 'Create your free account' : mode === 'signin' ? 'Welcome back' : 'Reset your password'}</h3>
      <p className="small">{mode === 'signup' ? 'Use your own email address. No ChatGPT account needed.' : mode === 'reset' ? 'We’ll email you a link to choose a new password.' : 'Sign in with your Mossy Friends email and password.'}</p>
      <form key={mode} onSubmit={e => { e.preventDefault(); const form = new FormData(e.currentTarget); const element = e.currentTarget; run(async () => {
        const result = await request('/api/auth', { action: mode, email: form.get('email'), password: form.get('password'), adult: form.get('adult') === 'on', policy: form.get('policy') === 'on' });
        element.reset();
        if (mode === 'reset') setMessage(result.message);
        else { await refresh(); if (mode === 'signup') setMessage(result.verificationSent ? 'Verification email sent. Check your inbox and spam folder.' : 'Your sign-in was created, but the email could not be sent. Use Resend verification email to try again.'); }
      }); }}>
        <label className="form-label">Email address<input type="email" name="email" autoComplete="email" maxLength={254} required /></label>
        {mode !== 'reset' && <label className="form-label">Password<input type="password" name="password" minLength={mode === 'signup' ? 12 : 1} maxLength={256} autoComplete={mode === 'signup' ? 'new-password' : 'current-password'} required />{mode === 'signup' && <span className="small">At least 12 characters.</span>}</label>}
        {mode === 'signup' && <><label className="check-label"><input type="checkbox" name="adult" required />I am an adult creating an account for myself.</label><label className="check-label"><input type="checkbox" name="policy" required />I acknowledge the Privacy Policy.</label></>}
        <button className="button primary full" disabled={busy}>{busy ? 'One moment…' : mode === 'signup' ? 'Create my free account' : mode === 'signin' ? 'Sign in' : 'Send reset email'}</button>
      </form>
      <div className="button-row"><button className="text-button" disabled={busy} onClick={() => { setMode(mode === 'signup' ? 'signin' : 'signup'); setError(''); setMessage(''); }}>{mode === 'signup' ? 'Already have an account? Sign in' : 'Create a new account'}</button>{mode !== 'reset' && <button className="text-button" disabled={busy} onClick={() => { setMode('reset'); setError(''); setMessage(''); }}>Forgot password?</button>}</div>
    </>}
    {message && <p role="status">{message}</p>}{error && <p className="form-error" role="alert">{error}</p>}
  </div>;
}
