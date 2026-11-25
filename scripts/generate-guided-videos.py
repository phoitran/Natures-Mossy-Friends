#!/usr/bin/env python3
"""Produce illustrated craft walkthroughs with original cheerful instrumental music.
No network calls. Authored SVGs and existing generated example galleries only.
Run from repo: python3 scripts/generate-guided-videos.py --id SPR-01
             python3 scripts/generate-guided-videos.py --all
"""
from pathlib import Path
import argparse, concurrent.futures, hashlib, json, math, os, re, subprocess, tempfile, wave
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'public/assets/videos'
WORK=Path('/tmp/nmf-guided-video-build'); WORK.mkdir(exist_ok=True)
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
INK='#153D2F'; BG='#FFF7F4'; GREEN='#CDE4B7'; MUTED='#315345'
MUSIC=ROOT/'assets/source/cheerful-woodland-loop.wav'
KIND='Illustrated video · cheerful instrumental music'
NS='{http://www.w3.org/2000/svg}'
ET.register_namespace('',NS[1:-1])

def run(args):
 p=subprocess.run([str(x) for x in args],capture_output=True,text=True)
 if p.returncode: raise RuntimeError('Command failed: '+str(args[0])+'\n'+p.stderr[-3000:])
 return p.stdout

def duration(path):
 return float(run(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',path]).strip())

def font(size,bold=False): return ImageFont.truetype(BOLD if bold else FONT,size)

def wrap(text,f,width):
 lines=[]; line=''
 for word in text.split():
  candidate=(line+' '+word).strip()
  if line and f.getlength(candidate)>width: lines.append(line); line=word
  else: line=candidate
 if line: lines.append(line)
 return lines

def text(draw,xy,value,size=30,width=440,bold=False,fill=INK,spacing=9):
 x,y=xy; f=font(size,bold)
 for line in wrap(value,f,width): draw.text((x,y),line,font=f,fill=fill);y+=size+spacing
 return y

# resvg-wasm does not ship system fonts. Convert exact authored SVG text to paths
# using DejaVu Sans so every original diagram label survives rendering.
def outline_text(source,dest):
 root=ET.parse(source).getroot()
 for parent in root.iter():
  for item in list(parent):
   if item.tag!=NS+'text': continue
   value=''.join(item.itertext()); size=float(item.get('font-size','20'))
   bold=int(item.get('font-weight','400'))>=600 if item.get('font-weight','400').isdigit() else item.get('font-weight')=='bold'
   ft=TTFont(BOLD if bold else FONT); cmap=ft.getBestCmap(); gs=ft.getGlyphSet();units=ft['head'].unitsPerEm
   scale=size/units
   advances=[ft['hmtx'].metrics[cmap.get(ord(c),'.notdef')][0] for c in value]
   total=sum(advances)*scale;x=float(item.get('x',0));y=float(item.get('y',0))
   if item.get('text-anchor')=='middle':x-=total/2
   elif item.get('text-anchor')=='end':x-=total
   group=ET.Element(NS+'g',{'fill':item.get('fill',INK),'transform':f'translate({x},{y}) scale({scale},{-scale})'})
   cursor=0
   for char,advance in zip(value,advances):
    name=cmap.get(ord(char),'.notdef'); pen=SVGPathPen(gs); gs[name].draw(pen)
    ET.SubElement(group,NS+'path',{'d':pen.getCommands(),'transform':f'translate({cursor},0)'})
    cursor+=advance
   parent.remove(item);parent.append(group);ft.close()
 ET.ElementTree(root).write(dest,encoding='utf-8',xml_declaration=True)

def base_frame(a,title,kicker='MAKE IT, ONE STEP AT A TIME'):
 im=Image.new('RGB',(1280,720),BG); d=ImageDraw.Draw(im)
 d.rounded_rectangle((-15,-24,1295,108),radius=40,fill='#DDF1E5')
 d.text((42,17),kicker,font=font(19,True),fill=INK)
 text(d,(40,47),title,36,1110,True,INK,3)
 # Small cheerful sun is a simple graphic accent, kept clear of instructions.
 d.ellipse((1186,23,1248,85),fill='#FFE6A4',outline='#315345',width=2)
 d.ellipse((1202,43,1207,49),fill=INK);d.ellipse((1227,43,1232,49),fill=INK)
 d.arc((1205,45,1230,69),0,180,fill=INK,width=3)
 d.ellipse((1196,54,1207,61),fill='#F3B8AC');d.ellipse((1227,54,1238,61),fill='#F3B8AC')
 d.rectangle((0,610,1280,720),fill='#10271F')
 return im,d

def example(gallery,index,size):
 source=Image.open(gallery).convert('RGB');w,h=source.size
 count=round(w/h)
 panel=source.crop((index*w//count,0,(index+1)*w//count,h))
 return panel.resize((size,size),Image.Resampling.LANCZOS)

def intro_frame(a,folder):
 im,d=base_frame(a,a['title'],'NATURES MOSSY FRIENDS · ILLUSTRATED GUIDE')
 im.paste(example(ROOT/f"public/assets/activities/{a['id']}.webp",0,470),(40,123))
 d.rounded_rectangle((58,548,491,584),radius=8,fill=INK)
 d.text((73,555),'AI-generated example',font=font(19,True),fill='white')
 y=text(d,(554,143),'Make a little wonder.',37,660,True)
 y=text(d,(554,y+14),a['description'],28,650)
 y=text(d,(554,y+20),'Before you begin',29,650,True)
 text(d,(554,y+7),'Gather your supplies. Make with a grown-up. Pause whenever you need more time.',27,650)
 im.save(folder/'scene-0.png');im.save(OUT/f"{a['id']}-poster.webp",quality=82)

def step_frame(a,step,i,folder):
 im,d=base_frame(a,f"{i} of 5 · {step['title']}")
 svg=Image.open(folder/f'diagram-{i}.png').convert('RGBA')
 im.paste(svg,(24,112),svg)
 d.rounded_rectangle((800,126,1258,596),radius=28,fill='#FFF0CB')
 y=text(d,(819,145),'Your turn',31,414,True)
 y=text(d,(813,y+12),step.get('littleTask') or step['title'],29,410)
 if step.get('adultTask'):
  y=text(d,(813,y+27),'Grown-up help',28,410,True)
  text(d,(813,y+10),step['adultTask'],26,410)
 else:
  y=text(d,(813,y+27),'Try a little more',28,410,True)
  text(d,(813,y+10),step.get('youngTask','Make it your own.'),26,410)
 d.text((811,561),'Pause, make, then play.',font=font(24,True),fill=INK)
 im.save(folder/f'scene-{i}.png')

def outro_frame(a,folder):
 im,d=base_frame(a,'Look what you can make!','FINISHED PROJECT IDEAS')
 count=len(a['examples'])
 size=190 if count>3 else 370
 for i in range(count):
  x=40+(i%3)*415;y=121+(i//3)*213 if count>3 else 128
  im.paste(example(ROOT/f"public/assets/activities/{a['id']}.webp",i,size),(x,y))
  if count>3:
   text(d,(x+200,y+57),a['examples'][i],24,190,True)
  else:d.text((x,510),f'Example {i+1}',font=font(26,True),fill=INK)
 text(d,(40,556),'AI-generated ideas. Your creation can look wonderfully different.',25,1200)
 im.save(folder/'scene-6.png')

def sentences(value):
 value=value.replace('–',' to ').replace('×',' by ').replace('cm','centimetres').replace('°C','degrees Celsius')
 return [x.strip() for x in re.split(r'(?<=[.!?])\s+',value) if x.strip()]

def caption_script(a):
 intro=f"Let's make {a['title']}. {a['description']} Make this project with a grown-up. Gather the supplies listed below the video. Pause whenever you need more time. {a['adultNote']}"
 scenes=[intro]
 for i,s in enumerate(a['steps'],1):
  words=f"Step {i}. {s['title']}. {s['text']}"
  if s.get('adultTask'):words+=f" Grown-up help. {s['adultTask']}"
  scenes.append(words)
 scenes.append(f"Here are {len(a['examples'])} ideas for your finished project. These example pictures were made with artificial intelligence. Your creation can look different. {a['cleanup']} {a['keep']} Well done. Take a moment to enjoy what you made.")
 return scenes

def caption_chunks(s,maxwords=14):
 words=s.split();return [' '.join(words[i:i+maxwords]) for i in range(0,len(words),maxwords)]

def make_audio(script,index,folder):
 # Reading-paced on-screen instructions only. No voice is generated.
 cues=[];elapsed=0.0;rate=24000
 for sentence in sentences(script):
  for chunk in caption_chunks(sentence,maxwords=12):
   sec=max(3.2,len(chunk.split())/2.2+0.8)
   cues.append({'start':elapsed,'end':elapsed+sec,'text':chunk})
   elapsed+=sec+0.25
 elapsed+=1.0
 out=folder/f'scene-{index}.wav'
 with wave.open(str(out),'wb') as f:
  f.setnchannels(1);f.setsampwidth(2);f.setframerate(rate)
  f.writeframes(b'\0\0'*round(elapsed*rate))
 return elapsed,cues

def replace_music(path,folder=None):
 if not MUSIC.exists():run(['python3',ROOT/'scripts/generate-cheerful-music.py'])
 length=duration(path);target=path.with_name(path.stem+'-instrumental.tmp.mp4')
 # Discard the old audio entirely. Copy video packets and map only the newly composed tune.
 run(['ffmpeg','-y','-hide_banner','-loglevel','error','-i',path,'-stream_loop','-1','-i',MUSIC,
      '-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','48k','-ar','24000','-ac','1',
      '-af',f'afade=t=out:st={max(0,length-1):.3f}:d=1','-t',f'{length:.6f}',
      '-metadata','comment=Original synthesized instrumental composition; no speech or sampled music',
      '-movflags','+faststart',target])
 os.replace(target,path)

def stamp(t,ass=False):
 h=int(t//3600);m=int(t//60)%60;s=t%60
 return f'{h}:{m:02}:{s:05.2f}' if ass else f'{h:02}:{m:02}:{s:06.3f}'

def ass_file(cues,path):
 header='''[Script Info]\nScriptType: v4.00+\nPlayResX: 1280\nPlayResY: 720\nWrapStyle: 0\n\n[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\nStyle: Default,DejaVu Sans,29,&H00FFFFFF,&H00FFFFFF,&H0010271F,&H0010271F,-1,0,0,0,100,100,0,0,1,0,0,2,48,48,18,1\n\n[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n'''
 for c in cues:
  value=c['text'].replace('{','').replace('}','')
  header+=f"Dialogue: 0,{stamp(c['start'],True)},{stamp(c['end'],True)},Default,,0,0,0,,{value}\n"
 path.write_text(header)

def visual_emphasis(a,index,cues,seconds):
 # The crown's authored step 3 has three exact construction panels. Reveal the
 # active movement in reading order while leaving the drawing itself unchanged.
 # Caption boundaries drive the emphasis, so words and visual focus stay aligned.
 if a['id']!='SPR-07' or index!=3:return []
 def cue_start(phrase,fallback):
  return next((c['start'] for c in cues if phrase in c['text'].lower()),fallback)
 wrap_start=cue_start('bring the hanging',seconds*.24)
 tail_start=cue_start('fold its long tail',seconds*.48)
 full_start=cue_start('gently snug the loop',seconds*.70)
 times=[0,wrap_start,tail_start,full_start]
 if not all(times[j]<times[j+1] for j in range(3)):
  raise ValueError('Crown motion emphasis must follow increasing caption times')
 # Native SVG bounds: (42/342/642, 140, 276, 390), rendered 760px wide.
 scale=760/960
 boxes=[(round(24+x*scale),round(112+140*scale),round(276*scale),round(390*scale)) for x in [42,342,642]]
 filters=[]
 for active,(start,end) in enumerate(zip(times,times[1:])):
  enable=f"gte(t,{start:.3f})*lt(t,{end:.3f})"
  for j,(x,y,w,h) in enumerate(boxes):
   colour='0xD58A29@1' if j==active else '0xFFF7F4@0.76'
   thickness='6' if j==active else 'fill'
   filters.append(f"drawbox=x={x}:y={y}:w={w}:h={h}:color={colour}:t={thickness}:enable='{enable}'")
 return filters

def produce(a):
 folder=WORK/a['id'];folder.mkdir(exist_ok=True);OUT.mkdir(exist_ok=True)
 svgfiles=[]
 for i,s in enumerate(a['steps'],1):
  target=folder/f'diagram-{i}.svg';outline_text(ROOT/'public'/s['diagram'].lstrip('/'),target);svgfiles.append(target)
 run(['node',ROOT/'scripts/generate-guided-videos.mjs',*svgfiles])
 intro_frame(a,folder)
 for i,s in enumerate(a['steps'],1):step_frame(a,s,i,folder)
 outro_frame(a,folder)
 allcues=[];chapters=[];elapsed=0;segments=[]
 for i,script in enumerate(caption_script(a)):
  sec,cues=make_audio(script,i,folder)
  title='Meet your project' if i==0 else 'Finished examples & tidy up' if i==6 else a['steps'][i-1]['title']
  chapters.append({'step':i,'start':round(elapsed,3),'title':title})
  ass=folder/f'scene-{i}.ass';ass_file(cues,ass)
  seg=folder/f'scene-{i}.mp4';segments.append(seg)
  filters=visual_emphasis(a,i,cues,sec)+[f'ass={ass}']
  run(['ffmpeg','-y','-hide_banner','-loglevel','error','-loop','1','-framerate','6','-i',folder/f'scene-{i}.png','-i',folder/f'scene-{i}.wav','-vf',','.join(filters),'-c:v','libx264','-threads','2','-preset','fast','-crf','30','-tune','stillimage','-r','6','-pix_fmt','yuv420p','-c:a','aac','-b:a','48k','-ar','24000','-ac','1','-af','apad','-t',f'{math.ceil(sec*6)/6:.6f}','-movflags','+faststart',seg])
  # Concat uses encoded video segment duration; use that timeline for exact chapter boundaries.
  actual=duration(seg)
  allcues.extend({**c,'start':c['start']+elapsed,'end':c['end']+elapsed} for c in cues)
  elapsed+=actual
 concat=folder/'concat.txt';concat.write_text('\n'.join(f"file '{p}'" for p in segments))
 final=OUT/f"{a['id']}.mp4"
 run(['ffmpeg','-y','-hide_banner','-loglevel','error','-f','concat','-safe','0','-i',concat,'-c','copy','-movflags','+faststart',final])
 replace_music(final,folder)
 vtt='WEBVTT\n\n'
 for n,c in enumerate(allcues,1):vtt+=f"{n}\n{stamp(c['start'])} --> {stamp(c['end'])}\n{c['text']}\n\n"
 (OUT/f"{a['id']}.vtt").write_text(vtt)
 meta={'id':a['id'],'durationSeconds':round(duration(final),3),'chapters':chapters,'video':f"/assets/videos/{a['id']}.mp4",'captions':f"/assets/videos/{a['id']}.vtt",'poster':f"/assets/videos/{a['id']}-poster.webp",'bytes':final.stat().st_size,'kind':KIND,'revision':hashlib.sha256(final.read_bytes()).hexdigest()[:12]}
 (folder/'metadata.json').write_text(json.dumps(meta,indent=2))
 print(json.dumps({'id':a['id'],'durationSeconds':meta['durationSeconds'],'bytes':meta['bytes']}),flush=True)
 return meta

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--id',action='append');ap.add_argument('--all',action='store_true');ap.add_argument('--workers',type=int,default=2);ap.add_argument('--skip-existing',action='store_true');ap.add_argument('--replace-audio',action='store_true');args=ap.parse_args()
 if args.replace_audio:
  existing=ROOT/'content/videos.json';meta=json.loads(existing.read_text())
  for item in meta:
   path=ROOT/'public'/item['video'].lstrip('/');replace_music(path)
   item.update(kind=KIND,bytes=path.stat().st_size,durationSeconds=round(duration(path),3),revision=hashlib.sha256(path.read_bytes()).hexdigest()[:12])
   temporary=existing.with_suffix('.json.tmp');temporary.write_text(json.dumps(meta,indent=2)+'\n');temporary.replace(existing)
   print(json.dumps({'id':item['id'],'audio':'original instrumental only','bytes':item['bytes']}),flush=True)
  return
 activities=json.loads((ROOT/'content/activities.json').read_text());selected=[a for a in activities if args.all or a['id'] in (args.id or [])]
 if not selected:ap.error('Use --all or --id ACTIVITY-ID')
 if args.skip_existing:selected=[a for a in selected if not (OUT/f"{a['id']}.mp4").exists()]
 metadata={}
 existing=ROOT/'content/videos.json'
 if existing.exists():metadata={x['id']:x for x in json.loads(existing.read_text())}
 with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
  futures=[ex.submit(produce,a) for a in selected]
  for future in concurrent.futures.as_completed(futures):
   result=future.result();metadata[result['id']]=result
   temporary=existing.with_suffix('.json.tmp')
   temporary.write_text(json.dumps([metadata[a['id']] for a in activities if a['id'] in metadata],indent=2)+'\n')
   temporary.replace(existing)

if __name__=='__main__':main()
