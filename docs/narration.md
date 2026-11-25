# Recorded read-aloud narration

The first batch covers A summer nature mandala (SUM-06), five steps and the little, young, and together variants. Generated on 23 November 2026 with ElevenLabs voice Shelley – Clear, Confident and British (4CrZuIW9am7gYAxgo2Af), Eleven v4. Each MP3 is a complete step, including its age-specific maker task and any grown-up help.

Recordings were created using the account’s free credits. The free plan permits noncommercial publication with attribution; the read-aloud control includes an elevenlabs.io credit. Reassess licensing before adding commercial use. No voice API key or generation call is shipped to visitors, and no subscription or recurring generation job was created.

## Adding a later batch

1. Generate the exact text from stepNarrationText in lib/step-narration.ts. Include every supported age variant and preserve grown-up directions.
2. Save MP3s in public/assets/narration, and add their text, activity, step, variant, source, provider and generation date to content/narration.json.
3. Run node tests/narration.test.mjs and TypeScript checks. Verify playback, stop, step changes and age changes in the browser.
4. Publish the source and matching assets together.

The player uses a recording only when its complete text still matches the current instructions. Missing or outdated recordings retain device speech synthesis; audio playback failures also fall back to it. Changing a route, step, age, guide or modal stops the current narration. Playing the video stops narration, and starting narration pauses the video.

Photo-guide videos retain their existing captions and background music; this batch changes only the step read-aloud feature.
