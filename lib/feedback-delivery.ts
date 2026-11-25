// FormSubmit's documented AJAX integration sends from the visitor's browser.
// This keeps the visitor on the page and lets the provider validate its origin.
export async function deliverFeedback(data: {kind:string;message:string;email?:string;page:string;activity?:string}) {
  let response: Response;
  try { response = await fetch('https://formsubmit.co/ajax/naturesmossyfriends@icloud.com', {
    method: 'POST', headers: { 'Content-Type':'application/json', Accept:'application/json' },
    credentials: 'omit', signal: AbortSignal.timeout(15000),
    body: JSON.stringify({ _subject:`Mossy Friends: ${data.kind}`, _template:'table', _captcha:'false',
      message:data.message, category:data.kind, page:data.page,
      ...(data.activity?{activity:data.activity}:{}), ...(data.email?{email:data.email,_replyto:data.email}:{}) }),
  }); } catch { throw new Error('We couldn’t reach the feedback email service. Please try again shortly.'); }
  let result: {success?:boolean|string;message?:string};
  try { result = await response.json(); } catch { throw new Error('The feedback email service is temporarily unavailable. Please try again shortly.'); }
  if (/activat|confirm your email|check your email/i.test(result.message||'')) throw new Error('Feedback email is being activated. Please try again shortly.');
  if (!response.ok || ![true,'true'].includes(result.success!)) throw new Error('We couldn’t send your feedback yet. Please try again shortly.');
}
