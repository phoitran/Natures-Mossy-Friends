# Contributing

1. Read the README, feature status and architecture. Discuss a behaviour or content change before broadening scope.
2. Work on a branch. Keep changes small and state the user-visible problem and resulting behaviour in the pull request.
3. Install with the lockfile, run relevant tests and type checking, and build before requesting review. Record checks that could not run.
4. Update the relevant documentation and add a focused regression check when fixing consequential behaviour. Do not add tests that merely repeat constants.

## Content changes

Preserve activity IDs used by saved projects. Archive old activities instead of reusing their IDs. Keep quantities, age tasks, adult help, diagrams and video captions consistent. If instruction text changes, regenerate or retire affected narration; never play a mismatched recording. Add original generation prompts/provenance and perform visual and physical review. Do not upload copied reference screenshots as published artwork.

## Database and media

Add a new migration rather than editing one that may already be applied. Preserve private/public separation and owner checks. Use artificial test photos without people or identifying details. Never commit user photos, database exports, tokens, API credentials or `.dev.vars`.

## Pull-request notes

Describe what changed, why, verification performed and unresolved limitations. Disclose material AI assistance, including code/media generation and how it was checked. Do not claim a live provider test, craft trial or licensing review unless it happened.
