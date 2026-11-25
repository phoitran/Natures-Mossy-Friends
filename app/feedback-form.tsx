'use client';
import { useState } from 'react';
import { CheckCircle2, Mail } from 'lucide-react';
import {deliverFeedback} from '../lib/feedback-delivery';

export default function FeedbackForm({ page, activity }: { page: string; activity?: string }) {
  const [kind, setKind] = useState('An activity idea');
  const [message, setMessage] = useState('');
  const [email, setEmail] = useState('');
  const [busy, setBusy] = useState(false);
  const [sent, setSent] = useState(false);
  const [error, setError] = useState('');
  if (sent) return <div className="feedback-success" role="status"><CheckCircle2 size={36} /><h3>Thanks for helping us grow.</h3><p>Your feedback has been sent to our team.</p><button className="button outline full" onClick={() => { setSent(false); setMessage(''); setEmail(''); }}>Share another idea</button></div>;
  return <form className="feedback-form" onSubmit={async e => {
    e.preventDefault(); if (!message.trim() || busy) return;
    const form = new FormData(e.currentTarget); setBusy(true); setError('');
    try {
      const response = await fetch('/api/feedback', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ kind, message, email, page, activity, website: form.get('website') }) });
      const data: any = await response.json();
      if (!response.ok) throw new Error(data.error || 'We couldn’t send that just now. Please try again.');
      if(data.deliver) await deliverFeedback({kind,message:message.trim(),email:email.trim(),page,activity});
      setSent(true);
    } catch (e) { setError(e instanceof Error ? e.message : 'We couldn’t send that just now. Please try again.'); }
    finally { setBusy(false); }
  }}>
    <p>Got an idea for a new activity, or something you’d like us to change? We’d love to hear it.</p>
    <label className="form-label" htmlFor="feedback-kind">What would you like to share?</label>
    <select id="feedback-kind" value={kind} disabled={busy} onChange={e => setKind(e.target.value)}>
      <option>An activity idea</option><option>A change I’d like</option><option>Something isn’t working</option><option>Other feedback</option>
    </select>
    <label className="form-label" htmlFor="feedback-message">Your idea or feedback</label>
    <textarea id="feedback-message" rows={5} maxLength={2000} required disabled={busy} value={message} onChange={e => setMessage(e.target.value)} placeholder="Tell us what you have in mind…" />
    <label className="form-label" htmlFor="feedback-email">Your email (optional, for a reply)</label>
    <input id="feedback-email" type="email" maxLength={254} autoComplete="email" disabled={busy} value={email} onChange={e => setEmail(e.target.value)} />
    <div className="feedback-trap" aria-hidden="true"><label>Leave this empty<input name="website" tabIndex={-1} autoComplete="off" /></label></div>
    <p className="feedback-context">About: {activity || 'this page'}</p>
    <button className="button primary full" type="submit" disabled={busy || !message.trim()}><Mail size={18} />{busy ? 'Sending…' : 'Send feedback'}</button>
    <p className="small feedback-delivery">Sends directly to naturesmossyfriends@icloud.com. No account needed. Please leave out children’s personal details.</p>
    {error && <p className="form-error" role="alert">{error} Your message is still here.</p>}
  </form>;
}
