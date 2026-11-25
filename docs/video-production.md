# Guided activity videos

The walkthroughs are illustrated videos with original cheerful instrumental music and readable timed instructions. There is no spoken voice in their audio. Each activity opens with a finished example, shows its five authored instruction diagrams and finishes with three example variations plus cleanup guidance. These are illustrated guides, not filmed demonstrations.

## Files and playback

- `public/assets/videos/{id}.mp4` — H.264, 1280×720, 6 fps, AAC mono instrumental music, fast-start metadata.
- `public/assets/videos/{id}.vtt` — timed English instruction captions.
- `public/assets/videos/{id}-poster.webp` — opening-frame poster.
- `content/videos.json` — `id`, `durationSeconds`, seven `chapters`, asset URLs, byte count, `kind`, and a twelve-character SHA-256 `revision` for cache invalidation.

Chapter 0 is the introduction, 1–5 are the five instructions, and 6 is the finished-example gallery and cleanup. Use native playback controls, no autoplay, a fullscreen option and chapter buttons. Captions are burned into a dedicated high-contrast band. The optional VTT is available for browser accessibility and download; displaying that track simultaneously can duplicate the built-in captions. The video does not change saved project progress.

The generated example galleries are labelled as inspiration, not physically tested outcomes. The craft guides still require practical review. New Fall 06–09 frames use mint, peach and butter-yellow framing with dark readable text, a friendly simple sun accent, and the new pastel cartoon instruction diagrams. Existing video pictures and caption timing are preserved when replacing their audio.

## Original music

`assets/source/cheerful-woodland-loop.wav` is an original sixteen-bar composition at 108 BPM, produced by `scripts/generate-cheerful-music.py`. A simple newly composed bell-like melody, soft bass and gently arpeggiated chords are synthesized from sine-wave partials. The score uses no external music, recordings, samples or voice synthesis. The loop has softened edges; every completed video fades its music at the end. Normal player volume and mute controls remain available.

Audio replacement explicitly maps the existing video's picture stream and only the new music input. Old audio streams are discarded completely. Video packets are copied without re-encoding for existing activities, so their diagrams and burned captions are preserved.

## Reproduce

Run from the repository root:

```sh
python3 scripts/generate-cheerful-music.py
python3 scripts/generate-guided-videos.py --replace-audio
python3 scripts/generate-guided-videos.py --all --skip-existing --workers 3
python3 scripts/generate-guided-videos.py --id FAL-06 --workers 1
```

The first command composes the instrumental. The second replaces audio in every MP4 listed in metadata, including archived activities, without changing their video or captions. The third creates missing activity videos. To change an existing video's illustrated content, regenerate that ID explicitly. Metadata is written atomically after each completed item. Final MP4 replacement uses a temporary file on the same filesystem.

Inputs are `content/activities.json`, exact authored SVG diagrams under `public/assets/steps`, and generated gallery WebPs. Frame assembly uses Pillow, fontTools to outline SVG text, the installed `@resvg/resvg-wasm` renderer and local ffmpeg. Music synthesis uses NumPy and standard WAV output. No network, text-to-speech or API calls occur during production. Working frames and intermediate silence tracks stay in `/tmp/nmf-guided-video-build`; only the instrumental is mapped into final videos.

New on-screen instructions are paced for reading, with phrases of at most twelve words, a minimum 3.2-second display and short gaps between phrases. Each scene is explicitly duration-bounded. Chapter and caption timestamps use the rendered scene durations. The original videos retain their existing caption timing after the audio-only change. No flashy transitions are used.

## Verification

Verify every expected MP4, VTT and poster; H.264 video and AAC audio; 1280×720 frame size; increasing chapter markers; captions ending before the video; and the SHA-256 revision matching the final MP4. Decode sample audio from every video and compare it with the locally composed music source to confirm the mapped track is the instrumental. Inspect representative intro, step and final-example frames. Results from the current production run are recorded below.

## Observed checks — November 22, 2026

All 24 MP4/VTT/poster sets passed verification, including archived activities. Every MP4 contains H.264 1280×720 video and AAC audio; audio/video endpoints differ by less than 0.3 seconds. All chapter sequences contain steps 0–6 in increasing time order, and final captions end before the video. All SHA-256 revisions match the delivered files. The 24 MP4s total 42.71 MB.

The first six seconds of each decoded audio track were numerically compared against the original composition: every correlation exceeded 0.999828. The production mapping explicitly excludes all original audio and includes only the instrumental source. Thus the delivered videos contain the newly composed tune, not the earlier spoken tracks. The new fall intro, step and final-example frames were inspected, including the corrected forked-post fairy-garden diagram. No temporary video files remain in the deployed asset directory.

## Spring additions — November 22, 2026 (America/Edmonton)

Four additional walkthroughs were produced from the final spring recipes, their exact authored pastel SVG diagrams, and the new generated example galleries. Every video opens with a finished example, shows five illustrated steps with reading-paced captions, and ends with all three example variations plus cleanup guidance. They use the same original instrumental source and contain no narration.

| Activity | Duration (seconds) | MP4 bytes | Revision |
| --- | ---: | ---: | --- |
| SPR-06 Meet the mud creatures | 327.210 | 3306157 | `2c81ce31efec` |
| SPR-07 Dandelion Crown | 374.543 | 3899696 | `ee54a4a70ddc` |
| SPR-08 Muddy Faces | 352.544 | 3679095 | `460f3ad08d73` |
| SPR-09 Spring Fairy Garden | 373.210 | 3875584 | `5bcdc673fcab` |

Crown step 3 begins at 159.5 seconds. Its three authored diagram panels receive progressive visual emphasis driven by caption boundaries: Cross for 0–10.68 seconds within the step, Wrap for 10.68–20.63, Lay alongside for 20.63–27.14, then the full diagram for the rest of the step. The other panels dim while one is emphasized. No source artwork is replaced or redrawn, and no chapter or caption timing changes are introduced. The effect applies only to SPR-07 step 3. Four decoded frames confirmed that each highlighted movement aligns with its corresponding text, followed by the full drawing.

All four final MP4/VTT/poster sets passed codec, dimensions, audio/video endpoint, increasing chapter, caption-end, file-size and SHA-256 revision checks. Their decoded opening audio matches the original instrumental with correlation 0.999828 each. All 72 previously delivered video/caption/poster files remain byte-identical. No temporary video files remain in the public asset directory.

Intro text and all twenty task/adult-help text panels passed measured layout bounds checks. Representative intro, step and final-example frames were visually inspected for all four activities. SPR-09 uses the final corrected diagram showing two separate low supports, a thin flat roof and a visible opening for the optional rock shelter. New source images and full generation prompts are documented in `docs/spring-image-prompts.md`.

## Summer additions — November 22, 2026 (America/Edmonton)

Four new walkthroughs use the final summer catalogue, twenty exact pastel SVG direction diagrams, and the four new original triptych galleries. They retain the same five-step structure, introductory finished example, three-example ending, reading-paced captions and original cheerful instrumental. No narration or additional animation was introduced. Only missing SUM-06 through SUM-09 media were rendered; the shared generator was unchanged.

| Activity | Duration (seconds) | MP4 bytes | Revision |
| --- | ---: | ---: | --- |
| SUM-06 A summer nature mandala | 285.210 | 2964292 | `28a1e6dc663b` |
| SUM-07 Rocky friends | 307.377 | 3179640 | `dea2d749d423` |
| SUM-08 Our wilderness creatures | 328.877 | 3398191 | `b9de6f529829` |
| SUM-09 Sandy Explorer | 348.877 | 3645341 | `a602927fd286` |

All four MP4/VTT/poster sets passed H.264/AAC codec, 1280×720 dimensions, audio/video endpoint alignment, increasing seven-chapter sequence, caption ending, metadata byte count and SHA-256 revision checks. Opening audio decoded from every video correlates 0.999828 with the original instrumental source. All 84 prior video/caption/poster files remain byte-identical, proving the previous 28 walkthroughs were preserved. No temporary public video files remain.

All four introduction text blocks and twenty task/adult-help panels passed measured layout checks. Intro, instruction and three-example ending frames were visually inspected for each activity, along with a decoded captioned instruction frame from the final SUM-06 MP4. No text overflow was observed. The SUM-08 sequence uses the final single-bark body/face wording and stone-and-leaf bird example. Sandy Explorer shows an open, shallow route, small low ridges and a little water in one channel. Image provenance and prompts are recorded in `docs/summer-image-prompts.md`.

## Winter additions and complete catalogue check — November 22, 2026 (America/Edmonton)

Three winter walkthroughs were rendered from the final catalogue and fifteen approved pastel SVG diagrams, with the same original instrumental, reading-paced captions and seven chapters. Each has an opening finished example, five construction steps, and three final example images. No other videos were rendered or changed.

| Activity | Duration (seconds) | MP4 bytes | Revision |
| --- | ---: | ---: | --- |
| WIN-06 Make a little snow man | 319.543 | 3079530 | `0e77bad565b2` |
| WIN-07 A pocket-sized snow village | 319.377 | 3123559 | `5aaf04ebe349` |
| WIN-08 Snowy Friends | 342.211 | 3370590 | `b999159101dc` |

All three intro layouts and fifteen task/adult-help panels passed measured bounds checks. Intro, instruction and final-example frames were visually inspected. The longer WIN-08 introduction fits above the caption band. The village uses solid snow models with supported lightweight twig roofs, shallow door impressions and stones at ground level; Snowy Friends shows a low leaf-eared mouse, a broad short-eared rabbit and a low turtle. Prompt provenance and the village image refinement are recorded in `docs/winter-image-prompts.md`.

The final validation covered all 35 catalogue videos, including archived activities: every MP4/VTT/poster exists; H.264/AAC, 1280×720, audio/video endpoints, metadata durations and byte counts, increasing chapters 0–6, caption ending times and SHA-256 revisions all pass. All 35 decoded opening audio samples correlate 0.999828 with the original instrumental source. The 96 files belonging to the earlier 32 walkthroughs remain byte-identical. All 35 catalogue IDs match video metadata; there are exactly 105 delivery files and no public temporary video files. Total MP4 size is 80,226,823 bytes (80.23 MB).

## Winter reference revision — current video versions

The following versions supersede the first WIN-06/07/08 renders above. The new snowman examples closely follow the user's three references, the village presents three distinct building styles, and Snowy Friends now includes all six requested animal designs. The approved final diagrams and catalogue were used for a targeted rebuild of those three videos only:

```sh
python3 scripts/generate-guided-videos.py --id WIN-06 --id WIN-07 --id WIN-08 --workers 2
```

The shared generator now accepts repeated `--id` arguments, detects the number of square panels in each gallery, and displays a six-example ending as a labelled three-column, two-row layout. The closing caption also uses the actual example count. These changes preserve the music-only pipeline, captions and seven-chapter structure.

| Activity | Duration (seconds) | MP4 bytes | Revision |
| --- | ---: | ---: | --- |
| WIN-06 Make a little snow man | 346.544 | 3356202 | `83551f1bc9d5` |
| WIN-07 A pocket-sized snow village | 329.376 | 3219320 | `8f7a4659c191` |
| WIN-08 Snowy Friends | 359.709 | 3543801 | `5fc0457f5b87` |

Measured layout checks passed for all three introductions, fifteen task/adult-help panels and six ending labels. Rendered frames were visually inspected, including WIN-06 step 4, WIN-07 step 3 and the complete six-example WIN-08 ending. A frame decoded from the final WIN-08 MP4 confirms all six images and labels are visible, with the caption “Here are 6 ideas for your finished project.” beneath them. No overflow or panel-cropping errors were observed. Snowman and animal reference provenance and exact prompts are in `docs/winter-reference-revision-prompts.md`.

All 35 final MP4/VTT/poster sets passed codec, dimensions, audio/video alignment, metadata duration and byte counts, increasing chapters, caption ending and SHA-256 revision checks. Every decoded audio sample correlates 0.999828 with the original instrumental. The 96 media files for the other 32 walkthroughs remain byte-identical. Catalogue IDs and metadata match exactly, with 105 delivery files and no public temporary video files. Current MP4 total: 80,772,467 bytes (80.77 MB). No further media or metadata writes remain pending.
