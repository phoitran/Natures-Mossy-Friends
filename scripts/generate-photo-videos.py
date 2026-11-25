#!/usr/bin/env python3
"""Render 75-second photo-step guides from six-panel generated photo sheets.

The sheets contain setup, then the five written activity steps, in row order.
Every source panel is fitted without cropping. No speech or artificial motion.
Run: python scripts/generate-photo-videos.py --all --workers 2
"""
from pathlib import Path
import argparse
import concurrent.futures
import hashlib
import json
import subprocess
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'public/assets/videos'
WORK = Path('/tmp/nmf-photo-videos')
MUSIC = ROOT / 'assets/source/cheerful-woodland-loop.wav'
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
INK = '#1C3E2C'
PAPER = '#FAFAF4'
GREEN = '#E5EDDE'
TIMES = [8, 11, 11, 11, 11, 11, 12]
KIND = 'Photo step video · cheerful instrumental music'


def run(args):
    result = subprocess.run([str(x) for x in args], capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr[-4000:])
    return result.stdout


def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT, size)


def wrap(value, f, width):
    lines, line = [], ''
    for word in value.split():
        candidate = (line + ' ' + word).strip()
        if line and f.getlength(candidate) > width:
            lines.append(line)
            line = word
        else:
            line = candidate
    if line:
        lines.append(line)
    return lines


def text(draw, xy, value, size, width, bottom, bold=False, fill=INK, spacing=8):
    x, y = xy
    f = font(size, bold)
    for line in wrap(value, f, width):
        assert f.getlength(line) <= width, f'Text exceeds its width: {line}'
        box = draw.textbbox((x, y), line, font=f)
        assert box[3] <= bottom, f'Text exceeds its height: {value}'
        draw.text((x, y), line, font=f, fill=fill)
        y += size + spacing
    return y


def title(draw, value):
    for size in [34, 32, 30, 28]:
        if len(wrap(value, font(size, True), 1204)) <= 2:
            return text(draw, (38, 43), value, size, 1204, 124, True, spacing=3)
    raise ValueError('Title too long: ' + value)


def base(value, kicker):
    im = Image.new('RGB', (1280, 720), PAPER)
    draw = ImageDraw.Draw(im)
    draw.rectangle((0, 0, 1280, 124), fill=GREEN)
    draw.text((38, 14), kicker, font=font(17, True), fill=INK)
    title(draw, value)
    draw.rectangle((0, 610, 1280, 720), fill='#143329')
    return im, draw


def panel(source, index):
    w, h = source.size
    assert w % 3 == 0 and h % 2 == 0, 'Photo sheet must have an exact 3 by 2 grid'
    col, row = index % 3, index // 3
    return source.crop((col*w//3, row*h//2, (col+1)*w//3, (row+1)*h//2))


def paste_contained(im, photo, box):
    x, y, width, height = box
    fitted = ImageOps.contain(photo, (width, height), Image.Resampling.LANCZOS)
    im.paste(fitted, (x + (width-fitted.width)//2, y + (height-fitted.height)//2))


def photo_frame(activity, photo, index, summary, path):
    heading = activity['title'] if index == 0 else f"{index} of 5 · {activity['steps'][index-1]['title']}"
    kicker = 'NATURES MOSSY FRIENDS · 75-SECOND PHOTO GUIDE' if index == 0 else 'LOOK. PAUSE. MAKE IT YOUR OWN.'
    im, draw = base(heading, kicker)
    paste_contained(im, photo, (32, 136, 824, 454))
    draw.rounded_rectangle((880, 140, 1248, 592), radius=22, fill=GREEN)
    y = text(draw, (902, 160), 'Before you begin' if index == 0 else 'Your turn', 28, 322, 225, True)
    y = text(draw, (902, y+20), summary, 25, 322, 450, spacing=9)
    text(draw, (902, 484), 'Pause while you make.', 22, 320, 548, True)
    text(draw, (902, 549), 'AI-generated photo steps', 17, 320, 586)
    im.save(path)
    return im


def outro_frame(activity, path):
    im, draw = base('Look what you can make!', 'FINISHED PROJECT IDEAS')
    source = Image.open(ROOT / f"public/assets/activities/{activity['id']}.webp").convert('RGB')
    count = len(activity['examples'])
    assert source.width == source.height*count
    for i in range(count):
        example = source.crop((i*source.height, 0, (i+1)*source.height, source.height))
        if count <= 3:
            x = 40+i*415
            paste_contained(im, example, (x, 139, 370, 370))
            text(draw, (x, 522), f'Example {i+1}', 23, 370, 565, True)
        else:
            x, y = 40+(i%3)*415, 136+(i//3)*213
            paste_contained(im, example, (x, y, 185, 185))
            text(draw, (x+198, y+36), activity['examples'][i], 22, 190, y+183, True)
    text(draw, (40, 573), 'AI-generated ideas. Your creation can look wonderfully different.', 20, 1200, 604)
    im.save(path)


def stamp(t, ass=False):
    h, m, s = int(t//3600), int(t//60)%60, t%60
    return f'{h}:{m:02}:{s:05.2f}' if ass else f'{h:02}:{m:02}:{s:06.3f}'


def ass_file(cues, path):
    result = '''[Script Info]\nScriptType: v4.00+\nPlayResX: 1280\nPlayResY: 720\nWrapStyle: 0\n\n[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\nStyle: Default,DejaVu Sans,28,&H00FFFFFF,&H00FFFFFF,&H00143329,&H00143329,-1,0,0,0,100,100,0,0,1,0,0,2,48,48,24,1\n\n[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n'''
    for cue in cues:
        lines = wrap(cue['text'], font(28, True), 1170)
        assert len(lines) <= 2, 'Caption needs more than two lines'
        value = r'\N'.join(lines).replace('{', '').replace('}', '')
        result += f"Dialogue: 0,{stamp(cue['start'], True)},{stamp(cue['end'], True)},Default,,0,0,0,,{value}\n"
    path.write_text(result)


def render(activity, captions, frames_only=False):
    ident = activity['id']
    folder = WORK / ident
    folder.mkdir(parents=True, exist_ok=True)
    source = Image.open(ROOT / f'public/assets/photo-steps/{ident}.webp').convert('RGB')
    for i in range(6):
        summary = 'Gather your supplies and make with a grown-up. Follow one small step at a time.' if i == 0 else ' '.join(captions['steps'][i-1])
        im = photo_frame(activity, panel(source, i), i, summary, folder/f'scene-{i}.png')
        if i == 0:
            im.save(OUT/f'{ident}-poster.webp', quality=86)
    outro_frame(activity, folder/'scene-6.png')
    if frames_only:
        return None
    scene_captions = [captions['intro'], *captions['steps'], captions['outro']]
    cues, chapters, elapsed = [], [], 0
    for i, (seconds, phrases) in enumerate(zip(TIMES, scene_captions)):
        assert len(phrases) == (3 if i == 6 else 2)
        chapters.append({'step': i, 'start': elapsed, 'title': 'Meet your project' if i == 0 else 'Finished examples & tidy up' if i == 6 else activity['steps'][i-1]['title']})
        for j, phrase in enumerate(phrases):
            cues.append({'start': elapsed+j*seconds/len(phrases), 'end': elapsed+(j+1)*seconds/len(phrases), 'text': phrase})
        elapsed += seconds
    ass_file(cues, folder/'captions.ass')
    concat = ''.join(f"file '{folder/f'scene-{i}.png'}'\nduration {seconds}\n" for i, seconds in enumerate(TIMES))
    concat += f"file '{folder/'scene-6.png'}'\n"
    (folder/'frames.txt').write_text(concat)
    final = OUT/f'{ident}.mp4'
    temporary = OUT/f'{ident}-photo.tmp.mp4'
    run(['ffmpeg', '-y', '-hide_banner', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', folder/'frames.txt', '-stream_loop', '-1', '-i', MUSIC,
         '-map', '0:v:0', '-map', '1:a:0', '-vf', f"ass={folder/'captions.ass'},fps=6", '-c:v', 'libx264', '-threads', '2', '-preset', 'fast', '-crf', '27', '-tune', 'stillimage', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '48k', '-ar', '24000', '-ac', '1', '-af', 'afade=t=out:st=74:d=1', '-t', '75', '-metadata', 'comment=AI-generated photo-step guide; original instrumental music; no spoken narration', '-movflags', '+faststart', temporary])
    temporary.replace(final)
    duration = float(run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', final]).strip())
    assert 74.9 <= duration <= 75.2
    vtt = 'WEBVTT\n\n' + ''.join(f"{i}\n{stamp(c['start'])} --> {stamp(c['end'])}\n{c['text']}\n\n" for i, c in enumerate(cues, 1))
    (OUT/f'{ident}.vtt').write_text(vtt)
    metadata = {'id': ident, 'durationSeconds': round(duration, 3), 'chapters': chapters, 'video': f'/assets/videos/{ident}.mp4', 'captions': f'/assets/videos/{ident}.vtt', 'poster': f'/assets/videos/{ident}-poster.webp', 'bytes': final.stat().st_size, 'kind': KIND, 'revision': hashlib.sha256(final.read_bytes()).hexdigest()[:12]}
    (folder/'metadata.json').write_text(json.dumps(metadata, indent=2))
    print(json.dumps({'id': ident, 'seconds': duration, 'bytes': metadata['bytes']}), flush=True)
    return metadata


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', action='append')
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--workers', type=int, default=2)
    parser.add_argument('--frames-only', action='store_true')
    args = parser.parse_args()
    activities = json.loads((ROOT/'content/activities.json').read_text())
    selected = [a for a in activities if not a.get('archived') and (args.all or a['id'] in (args.id or []))]
    if not selected:
        parser.error('Select --all or one or more --id values.')
    captions = json.loads((ROOT/'content/short-video-captions.json').read_text())
    metadata = {a['id']: a for a in json.loads((ROOT/'content/videos.json').read_text())}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(render, activity, captions[activity['id']], args.frames_only) for activity in selected]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                metadata[result['id']] = result
    if not args.frames_only:
        path = ROOT/'content/videos.json'
        temporary = path.with_suffix('.json.tmp')
        temporary.write_text(json.dumps([metadata[a['id']] for a in activities], indent=2)+'\n')
        temporary.replace(path)


if __name__ == '__main__':
    main()
