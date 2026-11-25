# Testing and verification

## Repeatable commands

Install locked dependencies first (`npm run install:ci`).

| Command | Scope |
| --- | --- |
| `npm test` | Runs all six JavaScript suites below, stopping on failure |
| `node tests/content.test.cjs` | Active and archived content, stable IDs, age eligibility, privacy text and asset references |
| `node tests/discovery.test.mjs` | Surprise filters, no immediate repeat and empty/single-choice cases |
| `node tests/routes.test.mjs` | Account, project, private-photo and gallery handlers, ownership, revisions, quotas and reporting |
| `node tests/auth.test.mjs` | Prepared Firebase mode against a simulated provider; configuration, verification, session and isolation checks |
| `node tests/feedback.test.mjs` | Feedback validation/throttling and simulated delivery responses |
| `node tests/narration.test.mjs` | Recorded text matching, coverage and asset references |
| `npm run typecheck` | TypeScript without emitting files |
| `npm run test:media` | All active/archived media, file hashes, durations, streams, captions and chapters |
| `npm run build` | Sites-compatible production bundle |
| `npm run build:standalone` | Independent-mode compilation, without deploying |

Python media checks need `python3 -m pip install -r requirements-dev.txt` and `ffprobe` on PATH. Video regeneration also needs FFmpeg. Test outputs go to ignored `outputs/` subdirectories. Tests use artificial identities and do not upload test creations to the public site.

## Continuous integration

`.github/workflows/ci.yml` installs Node 24 dependencies, runs JavaScript/type/media checks and builds both modes. It has read-only repository permissions and contains no deployment credentials or deploy step. A workflow file is not evidence that a GitHub run passed: inspect the repository's Actions results after upload. Local results are recorded separately in [EXPORT_VERIFICATION.md](EXPORT_VERIFICATION.md).

## Required manual acceptance

Before opening a new deployment to real users, verify:

1. Guest browse, each filter and Surprise me with a single eligible result and empty results.
2. Every active activity, five steps, images, video seeking, captions, narration/fallback and printing on a phone and desktop.
3. Keyboard focus, dialogs, larger text, readable contrast, screen-reader labels and reduced motion. No formal accessibility audit is claimed.
4. Guest progress after reload and explicit backup/import when the site origin changes.
5. Real account signup/sign-in/verification/reset as applicable, using two independent adults/test accounts.
6. Private image access denied from the other account; explicit public sharing, withdrawal, reporting and deletion.
7. Actual feedback receipt at the configured monitored mailbox, including activation/failure behaviour.
8. Account deletion, quota release, interrupted cleanup and recovery. No live deletion should be tested on a real user's only account.
9. Hands-on trials of the physical activity directions, joins, materials and cleanup, with representative age groups and adult review.

A passing handler test does not establish browser compatibility, real mail delivery, production provider configuration, semantic photo moderation or physical craft safety. `docs/QA.md` is a historical log with older superseded behaviour; use this export report and current source for current claims.
