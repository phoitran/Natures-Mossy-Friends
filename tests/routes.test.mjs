import {build} from 'esbuild';
import {DatabaseSync} from 'node:sqlite';
import {readFileSync,readdirSync,mkdirSync,writeFileSync} from 'node:fs';
import assert from 'node:assert/strict';
const sql=new DatabaseSync(':memory:');
for(const file of readdirSync('drizzle').filter(f=>f.endsWith('.sql')).sort())sql.exec(readFileSync('drizzle/'+file,'utf8').replaceAll('--> statement-breakpoint',''));
const objects=new Map();
const DB={prepare(query){let params=[];const statement={bind(...values){params=values;return statement;},async first(){return sql.prepare(query).get(...params)||null;},async all(){return {results:sql.prepare(query).all(...params)};},async run(){const r=sql.prepare(query).run(...params);return {meta:{changes:Number(r.changes)}};}};return statement;},async batch(statements){const result=[];for(const s of statements)result.push(await s.run());return result;}};
globalThis.__qaEnv={DB,PRIVACY_CONTACT_EMAIL:'privacy@example.invalid',BUCKET:{async put(k,b){objects.set(k,b);},async get(k){return objects.has(k)?{body:objects.get(k)}:null;},async delete(k){objects.delete(k);}}};
mkdirSync('outputs/route-tests',{recursive:true});
for(const name of ['account','projects','photos','creations'])await build({entryPoints:[`app/api/${name}/route.ts`],outfile:`outputs/route-tests/${name}.mjs`,bundle:true,platform:'node',format:'esm',plugins:[{name:'test-bindings',setup(b){b.onResolve({filter:/^(cloudflare:workers|next\/headers)$/},a=>({path:a.path,namespace:'qa'}));b.onLoad({filter:/.*/,namespace:'qa'},a=>({contents:a.path==='cloudflare:workers'?'export const env=globalThis.__qaEnv;':'export async function headers(){return globalThis.__qaRequest.headers;} export async function cookies(){throw new Error("Unexpected standalone auth in Sites mode");}',loader:'js'}));}}]});
const routes={};for(const name of ['account','projects','photos','creations'])routes[name]=await import(`../outputs/route-tests/${name}.mjs`);
let checks=0;
async function call(route,method='GET',data,user='test-owner-a',search='',origin='https://local.test',raw,extraHeaders={}){const headers={Origin:origin,...extraHeaders};if(user){headers['oai-authenticated-user-id']=user;headers['oai-authenticated-user-email']=`${user}@example.invalid`;}let body;if(raw){body=raw;headers['Content-Type']='image/jpeg';}else if(data!==undefined){body=JSON.stringify(data);headers['Content-Type']='application/json';}globalThis.__qaRequest=new Request(`https://local.test/api/${route}${search}`,{method,headers,body});const r=await routes[route][method](globalThis.__qaRequest);return {status:r.status,data:r.headers.get('content-type')?.includes('json')?await r.json():new Uint8Array(await r.arrayBuffer())};}
function eq(actual,want,label){assert.deepEqual(actual,want,label);checks++;console.log('PASS',label);}
eq((await call('projects','GET',undefined,null)).status,401,'anonymous project access rejected');
eq((await call('account','POST',{adult:true,policy:true},'test-owner-a','','https://other.test')).status,403,'cross-origin mutation rejected');
eq((await call('account','POST',{adult:false,policy:true})).status,400,'adult acknowledgement required');
for(const user of ['test-owner-a','test-owner-b'])eq((await call('account','POST',{adult:true,policy:true,name:'Test'},user)).status,200,'adult account created');
eq((await call('account')).data.account,true,'account persists');
let p={id:crypto.randomUUID(),activityId:'SPR-01',variant:'young',step:0,status:'in-progress'};
let r=await call('projects','POST',p);eq(r.status,200,'project created');p.revision=r.data.revision;
eq((await call('projects')).data.projects.length,1,'owner sees saved project');
eq((await call('projects','GET',undefined,'test-owner-b')).data.projects.length,0,'another owner cannot list project');
eq((await call('projects','POST',p,'test-owner-b')).status,404,'another owner cannot overwrite project');
p.step=1;r=await call('projects','POST',p);eq(r.status,200,'progress updated');
eq((await call('projects','POST',p)).status,409,'stale revision rejected');
eq((await call('projects','POST',{kind:'favourite',activityId:'WIN-01',saved:true})).status,200,'favourite saved separately');
// Minimal metadata-free JPEG structural fixture; route tests do not claim decoder compatibility.
const jpeg=Uint8Array.from([255,216,255,224,0,2,255,192,0,17,8,0,32,0,32,3,1,17,0,2,17,0,3,17,0,255,218,0,2,255,217]);
eq((await call('photos','POST',undefined,'test-owner-a','?project='+p.id,'https://local.test',new Uint8Array([1,2,3]))).status,400,'invalid bytes rejected');
eq((await call('photos','POST',undefined,'test-owner-b','?project='+p.id,'https://local.test',jpeg)).status,404,'upload requires project ownership');
const ids=[];for(let i=0;i<3;i++){r=await call('photos','POST',undefined,'test-owner-a','?project='+p.id,'https://local.test',jpeg);eq(r.status,200,'private photo stored');ids.push(r.data.id);}
eq((await call('photos','POST',undefined,'test-owner-a','?project='+p.id,'https://local.test',jpeg)).status,400,'three-photo limit enforced');
eq((await call('photos','GET',undefined,'test-owner-a','?id='+ids[0])).status,200,'owner retrieves private photo');
eq((await call('photos','GET',undefined,'test-owner-b','?id='+ids[0])).status,404,'another owner cannot retrieve photo');
eq((await call('photos','GET',undefined,null,'?id='+ids[0])).status,401,'anonymous photo access rejected');
eq((await call('photos','DELETE',undefined,'test-owner-a','?id='+ids[0])).status,200,'photo deletion works');
eq((await call('photos','GET',undefined,'test-owner-a','?id='+ids[0])).status,404,'deleted photo unavailable');
eq((await call('projects','DELETE',undefined,'test-owner-b','?id='+p.id)).status,404,'another owner cannot delete project');
eq((await call('projects','DELETE',undefined,'test-owner-a','?id='+p.id)).status,200,'project deletion works');
eq((await call('photos','GET',undefined,'test-owner-a','?id='+ids[1])).status,404,'project deletion removes attached photos');
eq((await call('projects')).data.favourites.length,1,'project deletion preserves favourites');
eq(objects.size,0,'storage objects removed');
eq(sql.prepare('SELECT photo_bytes FROM accounts WHERE id=?').get('test-owner-a').photo_bytes,0,'storage quota released');
eq((await call('account','DELETE')).status,200,'account deletion works');
eq((await call('account')).data.account,false,'deleted account unavailable');
// Fall replacement IDs must save correctly while earlier project IDs remain valid.
for(const activityId of ['FAL-06','FAL-07','FAL-08','FAL-09']){
 const payload={id:crypto.randomUUID(),activityId,variant:'young',step:0,status:'in-progress'};
 eq((await call('projects','POST',payload,'test-owner-b')).status,200,activityId+' new fall project accepted');
 eq((await call('projects','POST',{kind:'favourite',activityId,saved:true},'test-owner-b')).status,200,activityId+' can be favourited');
}
eq((await call('projects','POST',{id:crypto.randomUUID(),activityId:'FAL-07',variant:'little',step:0,status:'in-progress'},'test-owner-b')).status,400,'advanced fairy garden rejects the younger pathway');
eq((await call('projects','POST',{kind:'favourite',activityId:'FAL-99',saved:true},'test-owner-b')).status,400,'unknown catalogue ID rejected');
const earlier={id:crypto.randomUUID(),activityId:'FAL-02',variant:'little',step:2,status:'in-progress'};
const oldResult=await call('projects','POST',earlier,'test-owner-b');
eq(oldResult.status,200,'earlier fall project can still be restored');
eq((await call('projects','POST',{...earlier,step:3,revision:oldResult.data.revision},'test-owner-b')).status,200,'earlier fall project keeps its progress');
for(const activityId of ['SPR-06','SPR-07','SPR-08','SPR-09']){
 const payload={id:crypto.randomUUID(),activityId,variant:'young',step:0,status:'in-progress'};
 eq((await call('projects','POST',payload,'test-owner-b')).status,200,activityId+' new spring project accepted');
 eq((await call('projects','POST',{kind:'favourite',activityId,saved:true},'test-owner-b')).status,200,activityId+' can be favourited');
}
for(const activityId of ['SPR-07','SPR-09'])eq((await call('projects','POST',{id:crypto.randomUUID(),activityId,variant:'little',step:0,status:'in-progress'},'test-owner-b')).status,400,activityId+' advanced guide rejects the younger pathway');
const oldSpring={id:crypto.randomUUID(),activityId:'SPR-01',variant:'young',step:2,status:'in-progress'};
const oldSpringResult=await call('projects','POST',oldSpring,'test-owner-b');
eq(oldSpringResult.status,200,'earlier spring project can still be restored');
eq((await call('projects','POST',{...oldSpring,step:3,revision:oldSpringResult.data.revision},'test-owner-b')).status,200,'earlier spring project keeps its progress');
for(const activityId of ['SUM-06','SUM-07','SUM-08','SUM-09']){
 const payload={id:crypto.randomUUID(),activityId,variant:'young',step:0,status:'in-progress'};
 eq((await call('projects','POST',payload,'test-owner-b')).status,200,activityId+' new summer project accepted');
 eq((await call('projects','POST',{kind:'favourite',activityId,saved:true},'test-owner-b')).status,200,activityId+' can be favourited');
}
eq((await call('projects','POST',{id:crypto.randomUUID(),activityId:'SUM-08',variant:'little',step:0,status:'in-progress'},'test-owner-b')).status,400,'wilderness creatures rejects younger pathway');
eq((await call('projects','POST',{id:crypto.randomUUID(),activityId:'SUM-09',variant:'together',step:0,status:'in-progress'},'test-owner-b')).status,200,'Sandy Explorer accepts the shared pathway');
const oldSummer={id:crypto.randomUUID(),activityId:'SUM-02',variant:'little',step:2,status:'in-progress'};
const oldSummerResult=await call('projects','POST',oldSummer,'test-owner-b');
eq(oldSummerResult.status,200,'earlier summer project can still be restored');
eq((await call('projects','POST',{...oldSummer,step:3,revision:oldSummerResult.data.revision},'test-owner-b')).status,200,'earlier summer project keeps its progress');
for(const activityId of ['WIN-06','WIN-07','WIN-08']){
 const payload={id:crypto.randomUUID(),activityId,variant:'young',step:0,status:'in-progress'};
 eq((await call('projects','POST',payload,'test-owner-b')).status,200,activityId+' new winter project accepted');
 eq((await call('projects','POST',{kind:'favourite',activityId,saved:true},'test-owner-b')).status,200,activityId+' can be favourited');
}
for(const activityId of ['WIN-07','WIN-08'])eq((await call('projects','POST',{id:crypto.randomUUID(),activityId,variant:'little',step:0,status:'in-progress'},'test-owner-b')).status,400,activityId+' advanced winter guide rejects younger pathway');
eq((await call('projects','POST',{id:crypto.randomUUID(),activityId:'WIN-06',variant:'together',step:0,status:'in-progress'},'test-owner-b')).status,200,'snow person accepts shared pathway');
const oldWinter={id:crypto.randomUUID(),activityId:'WIN-01',variant:'little',step:2,status:'in-progress'};
const oldWinterResult=await call('projects','POST',oldWinter,'test-owner-b');
eq(oldWinterResult.status,200,'earlier winter project can still be restored');
eq((await call('projects','POST',{...oldWinter,step:3,revision:oldWinterResult.data.revision},'test-owner-b')).status,200,'earlier winter project keeps its progress');

// Public gallery is separate from private project photos and requires explicit sharing.
const share=(activityId='WIN-06',user='test-owner-a',confirmed=true,bytes=jpeg)=>call('creations','POST',undefined,user,'?activity='+activityId,'https://local.test',bytes,confirmed?{'X-Share-Confirmed':'yes'}:{});
eq((await call('account','POST',{adult:true,policy:true},'test-owner-a')).status,200,'gallery owner account created');
eq((await call('creations','GET',undefined,null,'?activity=WIN-06')).data.creations,[],'anonymous visitor sees an empty real gallery');
eq((await call('creations','GET',undefined,null,'?mine=1')).status,401,'private gallery shelf requires identity');
eq((await share('WIN-06',null)).status,401,'anonymous public upload rejected');
eq((await share('WIN-06','test-owner-a',false)).status,400,'explicit public sharing acknowledgement required');
eq((await share('BAD-99')).status,400,'public upload requires known activity');
eq((await share('WIN-06','test-owner-a',true,new Uint8Array([1,2,3]))).status,400,'public gallery rejects invalid image bytes');
eq((await call('creations','POST',undefined,'test-owner-a','?activity=WIN-06','https://other.test',jpeg,{'X-Share-Confirmed':'yes'})).status,403,'cross-origin public upload rejected');
let shared=await share();eq(shared.status,200,'completed creation published after explicit choice');const sharedId=shared.data.id;
let publicRows=(await call('creations','GET',undefined,null,'?activity=WIN-06')).data.creations;
eq(publicRows.length,1,'creation appears on matching activity');eq(publicRows[0].mine,false,'anonymous gallery does not mark ownership');
eq(Object.keys(publicRows[0]).sort(),['activityId','createdAt','id','mine','state'],'public gallery exposes no names emails owner ids or object keys');
eq((await call('creations','GET',undefined,null,'?activity=SUM-06')).data.creations.length,0,'public gallery filters by activity');
eq((await call('creations','GET',undefined,null,'?id='+sharedId)).status,200,'anonymous visitor can view explicitly public photo');
eq((await call('creations','GET',undefined,'test-owner-a','?mine=1')).data.creations[0].mine,true,'owner sees shared photo on own shelf');
eq((await call('creations','PATCH',{id:sharedId,action:'private'},'test-owner-b')).status,404,'another account cannot withdraw photo');
eq((await call('creations','DELETE',undefined,'test-owner-b','?id='+sharedId)).status,404,'another account cannot delete gallery photo');
eq((await call('creations','PATCH',{id:sharedId,action:'private'})).status,200,'owner can make shared creation private');
eq((await call('creations','GET',undefined,null,'?id='+sharedId)).status,404,'private gallery photo denied to public even by id');
eq((await call('creations','GET',undefined,'test-owner-b','?id='+sharedId)).status,404,'private gallery photo denied to other adult');
eq((await call('creations','GET',undefined,'test-owner-a','?id='+sharedId)).status,200,'owner retains photo after making it private');
eq((await call('creations','PATCH',{id:sharedId,action:'public'})).status,400,'republishing requires renewed explicit choice');
eq((await call('creations','PATCH',{id:sharedId,action:'public',confirmed:true})).status,200,'owner can explicitly share private creation again');
eq((await call('creations','PATCH',{id:sharedId,action:'report',reason:'privacy'},null)).status,401,'report requires adult account');
eq((await call('creations','PATCH',{id:sharedId,action:'report',reason:'invalid'},'test-owner-b')).status,400,'report reason validated');
eq((await call('creations','PATCH',{id:sharedId,action:'report',reason:'privacy'},'test-owner-b')).status,200,'report hides public photo');
eq((await call('creations','GET',undefined,null,'?id='+sharedId)).status,404,'reported photo unavailable publicly');
eq((await call('creations','GET',undefined,'test-owner-a','?mine=1')).data.creations[0].state,'hidden','owner receives reported-photo status');
eq((await call('creations','PATCH',{id:sharedId,action:'public',confirmed:true})).status,409,'reported photo cannot be republished');
await call('creations','PATCH',{id:sharedId,action:'private'});
eq((await call('creations','PATCH',{id:sharedId,action:'public',confirmed:true})).status,409,'privacy toggle cannot clear reported status');
const oldDelete=globalThis.__qaEnv.BUCKET.delete;globalThis.__qaEnv.BUCKET.delete=async()=>{throw new Error('test storage failure');};
eq((await call('creations','DELETE',undefined,'test-owner-a','?id='+sharedId)).status,500,'storage deletion failure reported');
globalThis.__qaEnv.BUCKET.delete=oldDelete;
eq((await call('creations','PATCH',{id:sharedId,action:'public',confirmed:true})).status,409,'failed deletion cannot clear reported status');
eq((await call('creations','DELETE',undefined,'test-owner-a','?id='+sharedId)).status,200,'owner deletes reported photo');
eq(sql.prepare('SELECT COUNT(*) AS n FROM creation_reports WHERE creation_id=?').get(sharedId).n,0,'deleting gallery photo removes reports');
const privateProject={id:crypto.randomUUID(),activityId:'WIN-06',variant:'little',step:5,status:'completed'};
await call('projects','POST',privateProject);const privateUpload=await call('photos','POST',undefined,'test-owner-a','?project='+privateProject.id,'https://local.test',jpeg);
eq(privateUpload.status,200,'private project photo still uploads normally');
eq((await call('creations','GET',undefined,null,'?activity=WIN-06')).data.creations.length,0,'private project photo never auto-publishes');
eq((await call('creations','GET',undefined,null,'?id='+privateUpload.data.id)).status,404,'public endpoint cannot expose a private project photo');
for(let i=0;i<6;i++)eq((await share()).status,200,'gallery photo under per-activity limit accepted');
const beforeQuota=sql.prepare('SELECT photo_bytes FROM accounts WHERE id=?').get('test-owner-a').photo_bytes;
const beforeObjects=objects.size;eq((await share()).status,400,'seventh gallery photo for same activity rejected');
eq(sql.prepare('SELECT photo_bytes FROM accounts WHERE id=?').get('test-owner-a').photo_bytes,beforeQuota,'failed limit attempt refunds storage reservation');eq(objects.size,beforeObjects,'failed limit attempt leaves no stored object');
const restoreBytes=beforeQuota;sql.prepare('UPDATE accounts SET photo_bytes=157286400 WHERE id=?').run('test-owner-a');
eq((await share('SUM-06')).status,400,'shared account storage quota enforced');sql.prepare('UPDATE accounts SET photo_bytes=? WHERE id=?').run(restoreBytes,'test-owner-a');
// Seed bounded fixtures only in isolated SQLite for cursor and maximum-count checks.
for(let i=0;i<15;i++)sql.prepare("INSERT INTO creations(id,owner_id,activity_id,object_key,bytes,state,created_at) VALUES(?,?,?,?,?,'public',?)").run('page-'+i,'test-owner-b','FAL-06','fixture-'+i,0,new Date(1000*i).toISOString());
const page1=(await call('creations','GET',undefined,null,'?activity=FAL-06')).data;eq(page1.creations.length,12,'public gallery page bounded to twelve photos');
const page2=(await call('creations','GET',undefined,null,'?activity=FAL-06&cursor='+encodeURIComponent(page1.nextCursor))).data;eq(page2.creations.length,3,'gallery cursor returns remaining photos');eq(new Set([...page1.creations,...page2.creations].map(x=>x.id)).size,15,'gallery pagination has no duplicates');
eq((await call('creations','GET',undefined,null,'?activity=FAL-06&cursor=bad')).status,400,'malformed cursor rejected');
const myCreation=(await call('creations','GET',undefined,'test-owner-a','?mine=1')).data.creations[0];await call('creations','PATCH',{id:myCreation.id,action:'report',reason:'privacy'},'test-owner-b');
eq((await call('account','DELETE',undefined,'test-owner-a')).status,200,'account deletion removes public and private uploads');
eq((await call('creations','GET',undefined,null,'?id='+myCreation.id)).status,404,'deleted-account creation unavailable publicly');eq(sql.prepare('SELECT COUNT(*) AS n FROM creations WHERE owner_id=?').get('test-owner-a').n,0,'account deletion removes gallery rows');eq((await call('photos','GET',undefined,'test-owner-a','?id='+privateUpload.data.id)).status,401,'account deletion also removes private photos');
console.log(`${checks} route tests passed using isolated SQLite and an in-memory object bucket.`);
