# Source-export verification — November 24, 2026

Original source: published site version **21**, commit `68ddd584154fa7324ea6554da003131b37a6cf59`.

## Checks performed for this package

| Check | Result |
| --- | --- |
| Source recovery | All 589 tracked files copied from the original source snapshot |
| Source fidelity | Application code and shipped assets unchanged; only original README, gitignore and package metadata/scripts changed |
| License | Existing MIT license and vendored notices preserved byte-for-byte |
| Dependencies | Locked install succeeded; dependency versions and integrity entries unchanged |
| Content and discovery | Passed catalogue/assets/eligibility and Surprise me suites |
| Server routes | 134 checks passed using isolated SQLite and in-memory object storage |
| Independent authentication | 47 checks passed against a simulated Firebase provider |
| Feedback | 16 checks passed; provider responses simulated |
| Narration | 15 recording assets/text variants passed matching and fallback checks |
| Media | All 35 active/archived media sets passed; active guides are 75 seconds |
| TypeScript | `npm run typecheck` passed |
| Sites build | `npm run build` passed |
| Local schema setup | All three documented SQL files applied successfully to a fresh local D1 database |
| Independent build | `npm run build:standalone` passed with example settings; not deployed |
| Export inspection | No common credential patterns found in scanned export text; secrets/runtime directories excluded |
| Documentation/package | Local documentation links, file inclusion and archive integrity checked during packaging |

Environment: Linux, Node **24.22.3**, npm **11.19.1**, Python with Pillow **13.0.0**, and installed FFmpeg/ffprobe. Check scripts and CI configuration are included so results can be repeated.

The install emitted deprecation/install-script notices and the builds emitted an environment npm proxy warning; the independent build also reported ineffective dynamic-import chunking warnings in Vinext. All commands above completed successfully. These messages are not a dependency vulnerability audit; no such audit is claimed.

## Limits

No new browser regression session, production sign-in/upload, real feedback-mail receipt, user-photo migration, physical craft trial or accessibility audit was performed during this export. No cloud deployment or live-site change was made. A successful standalone compilation does not establish configured independent signup.

The requested GitHub owner is **phoitran**, but the available connection belongs to **dare2feel** and exposes no phoitran repositories. GitHub's browser also required sign-in. The package is ready to upload; it has not been published into that account. The included Actions workflow has not run on GitHub yet.

## Package contents and integrity

`EXPORT_METADATA.json` records the source baseline and intentional export changes. `SHA256SUMS.txt` lists every packaged file except itself, using paths relative to the project folder. All media and editable originals are included. Dependencies, compiled output, Git history, credentials, local databases and real user-uploaded photos are excluded.
