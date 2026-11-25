# Short photo-step videos

The fifteen active guides use 75-second photo-step videos. Their detailed written instructions and cartoon instruction diagrams remain available separately. Twenty archived guides retain their original media.

Each guide uses a generated six-panel photo sheet: setup, then the five written construction steps, in reading order. The renderer fits each entire source panel into the video without cropping or adding simulated hand movement. These are labelled AI-generated photo guides, not recordings of tested physical builds.

The timeline has seven chapters: setup at 0 seconds, steps at 8, 19, 30, 41 and 52 seconds, then finished examples and cleanup at 63 seconds. Two short caption cues accompany each setup/step chapter; three accompany the ending. All 15 cues are burned into the video and supplied in an English VTT track. The full written guide contains the complete materials, age-specific roles, grown-up help and cleanup instructions.

`content/short-video-captions.json` contains the reviewed short scripts. `scripts/generate-photo-videos.py` renders frames with measured text bounds, encodes 1280×720 H.264 video, and maps only the original cheerful instrumental to AAC audio. The final second fades out. No spoken narration or sampled music is added. Metadata includes duration, chapter positions, byte size and the first twelve characters of the MP4 SHA-256 hash for cache invalidation.

Rebuild all active guides with:

```bash
python scripts/generate-photo-videos.py --all --workers 2
```

Use repeated `--id` arguments for a subset or `--frames-only` for layout checks. The renderer never selects archived guides.

Validation includes text bounds for all 75 step panels and all 225 caption cues, uncropped source-panel layout, exact chapter order, duration, codec/dimensions, caption timing, audio and revision hashes. Asset prompt records are in `docs/photo-steps-spring.md`, `docs/photo-steps-summer.md`, `docs/photo-steps-fall.md` and `docs/photo-steps-winter.md`.

## Completed validation

- All fifteen active MP4 files are exactly 75.0 seconds, with the seven chapter positions above and fifteen caption cues each.
- `python tests/media.test.py` passes for all 35 active and archived guides, including source gallery dimensions, the new six-panel sheets, streams, caption timing, posters, duration and SHA-256 revision metadata.
- Decoded samples from every new video match the original instrumental with correlation 0.999851. No voice track is present.
- The sixty media files and twenty metadata records belonging to archived guides are byte-identical to the prior Git revision.
- All 75 step text panels and 225 caption cues pass measured width/height checks. A decoded representative frame from every active video passed visual review, plus the Crown wrap close-up and the six-animal ending.
