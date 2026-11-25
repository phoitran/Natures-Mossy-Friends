import recordings from '../content/narration.json';

type Step = {title:string;text:string;littleTask:string;youngTask:string;adultTask?:string};

export function stepNarrationText(step:Step,index:number,variant:string){
 const role=variant==='together'?`Little Makers. ${step.littleTask} Young Creators. ${step.youngTask}`:variant==='little'?step.littleTask:step.youngTask;
 return `Step ${index+1}. ${step.title}. ${step.text} Your maker’s part. ${role}${step.adultTask?' Grown-up help. '+step.adultTask:''}`;
}

export function findStepNarration(activityId:string,index:number,variant:string,text:string){
 // Never play an outdated recording after the written directions change.
 return recordings.find(recording=>recording.activityId===activityId&&recording.step===index+1&&recording.variant===variant&&recording.text===text);
}
