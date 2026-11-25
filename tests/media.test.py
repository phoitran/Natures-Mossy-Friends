"""Verify the shipped tutorial media, chapter boundaries and caption coverage."""
import json,re,subprocess,hashlib
from pathlib import Path
from PIL import Image
activities=json.loads(Path('content/activities.json').read_text())
active_ids={a['id'] for a in activities if not a.get('archived')}
media=json.loads(Path('content/videos.json').read_text())
assert len(media)==len(activities),'Every active and archived guide needs its matching media'
assert {x['id'] for x in media}=={x['id'] for x in activities}
for activity in activities:
 with Image.open(Path('public/assets/activities')/(activity['id']+'.webp')) as gallery:
  assert gallery.width==gallery.height*len(activity['examples']),activity['id']+' gallery panels do not match example labels'
for item in media:
 ident=item['id']; root=Path('public/assets/videos')
 assert item.get('revision')==hashlib.sha256((root/(ident+'.mp4')).read_bytes()).hexdigest()[:12],ident+' stale media revision'
 for ext in ['.mp4','.vtt','-poster.webp']: assert (root/(ident+ext)).is_file(),ident+ext
 info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(root/(ident+'.mp4'))]))
 assert any(x['codec_type']=='audio' for x in info['streams']),ident+' lacks music'
 assert 'instrumental' in item['kind'].lower(),ident+' must use music instead of narration'
 video=next(x for x in info['streams'] if x['codec_type']=='video')
 assert video['width']>=960 and video['height']>=720
 duration=float(info['format']['duration']);assert duration>45,ident+' unexpectedly short'
 if ident in active_ids:
  assert 60<=duration<=90,ident+' active guide must stay within 60–90 seconds'
  assert 'photo step' in item['kind'].lower(),ident+' active guide must use the new photo steps'
  with Image.open(Path('public/assets/photo-steps')/(ident+'.webp')) as sheet:
   assert sheet.width%3==0 and sheet.height%2==0,ident+' photo sheet needs six equal panels'
 assert abs(duration-item['durationSeconds'])<1
 assert [x['step'] for x in item['chapters']]==list(range(7)),ident+' incomplete chapters'
 assert item['chapters'][0]['start']==0
 assert all(0<=c['start']<duration for c in item['chapters'])
 assert all(x['start']<y['start'] for x,y in zip(item['chapters'],item['chapters'][1:]))
 captions=(root/(ident+'.vtt')).read_text();assert captions.startswith('WEBVTT')
 cues=re.findall(r'(\d\d):(\d\d):(\d\d\.\d+) --> (\d\d):(\d\d):(\d\d\.\d+)',captions)
 assert len(cues)>=15,ident+' insufficient caption coverage'
 for h,m,s,eh,em,es in cues:
  start=3600*int(h)+60*int(m)+float(s);end=3600*int(eh)+60*int(em)+float(es)
  assert 0<=start<end<=duration+.5,ident+' invalid caption timing'
 print(f'PASS {ident}: {duration:.1f}s, 7 chapters, {len(cues)} caption cues, audio + video')
print(f'PASS: all {len(media)} music-backed guides, posters and caption tracks validated.')
