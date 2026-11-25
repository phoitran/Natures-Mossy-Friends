import {build} from 'esbuild';
import {DatabaseSync} from 'node:sqlite';
import {mkdirSync} from 'node:fs';
import assert from 'node:assert/strict';
const sql=new DatabaseSync(':memory:');sql.exec('CREATE TABLE auth_attempts(id TEXT PRIMARY KEY,attempts INTEGER,expires_at INTEGER)');
const DB={prepare(query){let params=[];const s={bind(...p){params=p;return s;},async first(){return sql.prepare(query).get(...params);},async run(){sql.prepare(query).run(...params);return {};}};return s;}};
globalThis.__feedbackEnv={DB};mkdirSync('outputs/feedback-tests',{recursive:true});
await build({entryPoints:['app/api/feedback/route.ts'],outfile:'outputs/feedback-tests/route.mjs',bundle:true,platform:'node',format:'esm',define:{__MOSSY_STANDALONE__:'false'},plugins:[{name:'bindings',setup(b){b.onResolve({filter:/^(cloudflare:workers|next\/headers)$/},a=>({path:a.path,namespace:'test'}));b.onLoad({filter:/.*/,namespace:'test'},a=>({contents:a.path==='cloudflare:workers'?'export const env=globalThis.__feedbackEnv;':'export async function headers(){throw new Error("Feedback must not require identity");} export async function cookies(){throw new Error("Feedback must not require identity");}',loader:'js'}));}}]});
const {POST}=await import('../outputs/feedback-tests/route.mjs');let delivery='ok',sent=[],checks=0;
globalThis.fetch=async(url,options)=>{sent.push({url,body:JSON.parse(options.body),headers:options.headers});if(delivery==='fail')throw new Error('offline');return Response.json(delivery==='activate'?{success:'true',message:'Check your email to activate your form'}:delivery==='rejected'?{success:'false',message:'rejected'}:{success:'true',message:'The form was submitted successfully'});};
const message={kind:'An activity idea',message:'Please add a little pinecone family.',page:'/activities/WIN-08',activity:'Snowy Friends',email:''};
async function call(body=message,origin='https://mossy.test'){const r=await POST(new Request('https://mossy.test/api/feedback',{method:'POST',headers:{Origin:origin,'Content-Type':'application/json','cf-connecting-ip':'192.0.2.5'},body:JSON.stringify(body)}));return {status:r.status,data:await r.json()};}
function eq(a,b,label){assert.deepEqual(a,b,label);checks++;}
const reset=()=>sql.exec('DELETE FROM auth_attempts');
eq((await call(message,'https://elsewhere.test')).status,403,'cross-origin submission rejected');
eq((await call({...message,kind:'arbitrary subject'})).status,400,'category allowlisted');
eq((await call({...message,message:' '})).status,400,'empty feedback rejected');
eq((await call({...message,message:'a'.repeat(2001)})).status,400,'message length bounded');
eq((await call({...message,email:'x@example.com\nBCC:evil@example.com'})).status,400,'header injection rejected');
eq((await call({...message,website:'spam'})).status,200,'honeypot silently dropped');eq(sent.length,0,'honeypot does not send email');
eq((await call({...message,to:'attacker@example.com',page:'/account?token=private',name:'Do not forward'})).data.deliver,true,'anonymous feedback passes validation without login');
eq((await call({...message,email:'reply@example.invalid'})).status,200,'optional reply email accepted');
await call();eq((await call()).status,429,'feedback flood limited');
await build({entryPoints:['lib/feedback-delivery.ts'],outfile:'outputs/feedback-tests/delivery.mjs',bundle:true,platform:'node',format:'esm'});
const {deliverFeedback}=await import('../outputs/feedback-tests/delivery.mjs');
await deliverFeedback(message);
eq(sent[0].url,'https://formsubmit.co/ajax/naturesmossyfriends@icloud.com','recipient fixed in AJAX delivery');
eq(Object.keys(sent[0].body).sort(),['_captcha','_subject','_template','activity','category','message','page'],'only intentional feedback fields sent');
await deliverFeedback({...message,email:'reply@example.invalid'});eq(sent[1].body._replyto,'reply@example.invalid','reply-to forwarded when requested');
for(const mode of ['activate','rejected','fail']){delivery=mode;await assert.rejects(()=>deliverFeedback(message));checks++;}
console.log(`Passed ${checks} feedback checks.`);
