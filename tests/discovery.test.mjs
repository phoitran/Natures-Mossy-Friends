import {build} from 'esbuild';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
const bundled=await build({entryPoints:['lib/discovery.ts'],bundle:true,platform:'node',format:'esm',write:false});
const {surpriseChoices,chooseSurprise}=await import('data:text/javascript;base64,'+Buffer.from(bundled.outputFiles[0].text).toString('base64'));
const activities=JSON.parse(readFileSync('content/activities.json','utf8'));
for(const season of ['all','spring','summer','fall','winter'])for(const age of ['all','little','young']){
 const choices=surpriseChoices(activities,season,age);
 assert.ok(choices.length>0);
 assert.ok(choices.every(a=>!a.archived&&(season==='all'||a.season===season)&&(age==='all'||a.ages.includes(age))));
 const first=chooseSurprise(choices,'',()=>0);assert.ok(choices.includes(first));
 const next=chooseSurprise(choices,first.id,()=>0);assert.ok(choices.includes(next));
 if(choices.length>1)assert.notEqual(next.id,first.id);
}
assert.deepEqual(surpriseChoices(activities,'winter','little').map(a=>a.id),['WIN-06']);
assert.equal(chooseSurprise([],''),undefined);
assert.equal(chooseSurprise([{id:'only',season:'spring',ages:['little']}],'only').id,'only');
console.log('PASS: Surprise me honours every season/age combination, excludes archived guides, avoids immediate repeats and handles single/empty choices.');
