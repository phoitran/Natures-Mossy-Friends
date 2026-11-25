import {build} from 'esbuild';
import assert from 'node:assert/strict';
import {readFileSync,statSync} from 'node:fs';
import {execFileSync} from 'node:child_process';
const bundled=await build({entryPoints:['lib/step-narration.ts'],bundle:true,platform:'node',format:'esm',write:false});
const {stepNarrationText,findStepNarration}=await import('data:text/javascript;base64,'+Buffer.from(bundled.outputFiles[0].text).toString('base64'));
const catalogue=JSON.parse(readFileSync('content/activities.json','utf8'));
const recordings=JSON.parse(readFileSync('content/narration.json','utf8'));
const keys=new Set();
for(const recording of recordings){
 const key=`${recording.activityId}/${recording.step}/${recording.variant}`;
 assert.ok(!keys.has(key),`Duplicate recording: ${key}`);keys.add(key);
 const activity=catalogue.find(a=>a.id===recording.activityId);
 assert.ok(activity&&!activity.archived);
 const step=activity.steps[recording.step-1];
 const text=stepNarrationText(step,recording.step-1,recording.variant);
 assert.equal(recording.text,text,`${key}: spoken and written instructions differ`);
 assert.equal(findStepNarration(activity.id,recording.step-1,recording.variant,text)?.src,recording.src);
 assert.equal(findStepNarration(activity.id,recording.step-1,recording.variant,text+' Updated.'),undefined,'Changed directions must fall back to the device voice');
 assert.ok(recording.src.startsWith('/assets/narration/'));
 const path='public'+recording.src;
 assert.ok(statSync(path).size>10000,`${key}: audio is missing or empty`);
 const media=JSON.parse(execFileSync('ffprobe',['-v','error','-show_entries','format=duration:stream=codec_name','-of','json',path]));
 assert.equal(media.streams[0].codec_name,'mp3');
 const duration=Number(media.format.duration);
 assert.ok(duration>text.length/35&&duration<text.length/5,`${key}: unexpected duration ${duration}`);
 assert.ok(text.includes(step.adultTask||step.text),'Grown-up directions must be preserved');
}
const mandala=catalogue.find(a=>a.id==='SUM-06');
for(const [index,step] of mandala.steps.entries())for(const variant of ['little','young','together']){
 assert.ok(findStepNarration(mandala.id,index,variant,stepNarrationText(step,index,variant)),`Missing ${index+1}/${variant}`);
}
assert.equal(findStepNarration('WIN-06',0,'little','any text'),undefined,'Other activities retain their device voice');
console.log(`PASS: ${recordings.length} playable narration files; every mandala step and age option, adult guidance, stale-text protection and fallback coverage.`);
