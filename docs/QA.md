# Verification — November 22, 2026

## Seasonal replacement and visual update

- The active catalogue contains 15 activities: four each for spring, summer and fall, plus three for winter. Twenty earlier seasonal guides remain archived, keeping existing project IDs and saved progress meaningful. Prior guide bodies were compared with the previous source revision and are unchanged.
- Fall filtering shows Make a Leafy Friend and Fall Mandalas for Little Makers; Young Creators also see Fall Fairy Garden and Meet your fall friends. The two shared fall guides have distinct younger/older roles.
- Four new original image triptychs provide 12 finished examples closely following the user's leaf-animal, fairy-garden, mandala and leaf-fairy references. Original uploads are not reused on the site.
- Twenty new pastel cartoon SVGs match the five steps in each new guide. All metadata and asset references validate. Representative images and the full 20-panel contact sheet were visually checked, including the forked twig roof supports and temporary mud-paste directions.
- Browser checks confirm the four-card Fall collection, correct age-filter results, instructions open by default after materials, clearly marked optional supplies, matching step changes, and the enlarged illustration dialog.
- Desktop instruction diagrams use their full available width with no 320-pixel height cap. Existing larger-text mode remains available with dark text on pale backgrounds.

## Spring update checks

- New spring discovery contains exactly Meet the mud creatures, Dandelion Crown, Muddy Faces and Spring Fairy Garden. Browser checks show two eligible Little Makers cards and all four Young Creators cards.
- The reference recording was inspected locally. The crown tutorial uses the same repeated stem wrap and an overlapping tucked join; it does not reuse the recording. The flower name is corrected to dandelion to match the supplied images.
- Twelve original generated spring examples and all 20 new cartoon panels were visually reviewed. The crown has distinct existing/new stem colours and Cross, Wrap, Lay alongside phases. The spring garden clearly leans against a tree; the alternate stone shelter has separate supports, a flat roof and a visible doorway.
- Browser checks confirm enlarged crown and garden diagrams, full materials, optional supplies and instructions visible after materials. The crown's nature note explicitly permits limited adult-approved flower picking.
- A preview guest Spring Fairy Garden project was started, advanced and reloaded; the page retained step 2 and one completed step.
- The preview crown video successfully jumped to chapter 3 at 159.5 seconds and played with a full 0–374.543-second seek range and no media error. Its timed panel emphasis was visible during playback.
- Desktop home and About totals are derived from active content rather than hardcoded. The current home features new Winter activities and uses the snow cottage hero; shared-making artwork uses the new rocky-friend gallery.

## Summer update checks

- The active summer lineup is exactly A summer nature mandala, Rocky friends, Our wilderness creatures and Sandy Explorer. Three guides support both age groups and shared making; wilderness creatures supports Young Creators only.
- Isolated route checks cover saving and favouriting all four new IDs, rejecting the younger wilderness pathway, accepting the shared sand pathway, and restoring/continuing earlier summer projects.
- All 28 earlier guide bodies were compared with the previous source revision and are unchanged. Only archival flags change discovery for the five replaced summer records.
- New content explicitly keeps rocky friends flat and loose, limits moss to already-detached material, and explains that shallow water channels may drain into sand. Sandy Explorer has a real entrance and route to the centre, low walls, optional shell/pebble/flower decoration and full cleanup.

- All 20 summer cartoon panels and 12 gallery examples were visually reviewed, including the sand maze entrance and decoration clearances. Browser checks confirm three younger and four older summer cards. A shared Sandy Explorer project retained step 2 and one completed step after reload. Its video jumped to the decoration chapter at 206 seconds, played without a media error, and had a full 0–348.877-second seek range.

## Winter update checks

- The active winter lineup is exactly Make a little snow man, A pocket-sized snow village and Snowy Friends. The snow person supports both age groups and shared making; village and animal sculpting are for Young Creators.
- Isolated route checks cover saving/favouriting the three new IDs, age eligibility, the shared snow-person pathway and earlier winter project restoration.

- Browser checks show one eligible Little Makers winter card and all three Young Creators cards. All nine winter gallery examples and all 15 pastel instruction panels were visually checked. The village examples show solid cottages with supported twig roofs, shallow door marks and stones at ground level; the snow animals use low bodies and broad joins.

- A guest snow-village project was started and advanced; after a reload it retained step 2 and one completed step. The enlarged roof diagram opens correctly and explains that solid snow supports the twigs.

- The preview village video jumped to chapter 3 at 146.334 seconds and played with a full 0–319.377-second seek range and no media error.

## Videos and audio

- All 35 active and archived guides have MP4s, posters, timed captions and seven valid chapter markers. Media checks verify video/audio streams, duration, caption bounds, and SHA-256 revision values used to prevent stale cached narration.
- Spoken video narration has been replaced with an original locally composed cheerful instrumental. New fall videos use pastel framing and the new cartoon diagrams. Separate, explicitly activated browser read-aloud remains available where supported.
- Browser playback of the new Fall Fairy Garden video was observed at Step 3: the chapter jumped to 151.67 seconds and advanced normally, with no media error and a full seekable range. Autoplay is disabled.
- Videos load into a browser Blob because the hosting asset proxy does not expose a usable byte-range seek window. Navigation aborts unfinished fetches and revokes the prior Blob URL.
- Captions are burned into each video. The optional native VTT track is not enabled by default, avoiding duplicate text.

## Code and saved data

- TypeScript checks pass.
- Content tests verify all 35 active/archived records, 108 example panels, 175 diagram files, the exact seasonal lineups, age eligibility and the supplied privacy contact.
- All 79 isolated route tests pass. They use the real route handlers with in-memory SQLite and an object-bucket substitute. Coverage includes ownership, origins, revision conflicts, upload limits, private retrieval, deletion, and saving/favouriting every new seasonal ID.
- Additional regression checks confirm the advanced fairy garden rejects an ineligible younger pathway, unknown IDs are rejected, and older seasonal progress can still be restored and continued.
- Earlier browser checks verified guest progress survives a reload, Make Together links work, and a 390 × 844 layout has no horizontal overflow. This revision retains the responsive layout and enlarges the fall diagrams within it.

## Limits

- Hosted authentication and actual phone-photo upload have not been exercised using the user's identity. Server tests validate handler logic, not the provider's live transport.
- Standalone email/password signup is still not connected; accounts use the supported ChatGPT identity flow.
- Device read-aloud depends on browser speech support. In the cloud browser it reported that no working voice was available; the illustrated instructions and captioned music video remained usable.
- These are draft craft guides, not physically tested or professionally reviewed. Generated examples are labelled inspiration.

## Winter reference fidelity revision

The Winter galleries now follow the supplied photographs more closely. The snowman gallery has the pine-cone-hat, classic carrot-nose and upside-down-boots examples. The village preserves the original first cottage panel and adds rounded sprig-topped houses with twig-bordered paths plus a distinct snow-block hamlet. Snowy Friends expands to six examples: mice, rabbits, cat with mouse, seated cat, bear and turtle. Gallery width and example count are checked together so every image crops correctly. Instructions and video examples have been updated to cover these variations.

All 12 revised gallery panels and all 15 Winter instruction panels passed visual review. The first village source panel is pixel-identical to the previous cottage. Browser checks confirmed the three village choices, the two-row six-animal gallery, and selection of the sixth image with the correct crop. The updated Snowy Friends video jumped to its finished-examples chapter at 308.35 seconds and played normally with all six examples, a full 0–359.709-second seek range and no media error.

The three rebuilt Winter videos pass the complete 35-guide media checks, including gallery dimensions, chapter/caption alignment, stream formats, revision hashes and file sizes. Decoded audio matches the original instrumental (correlation 0.999828). All 96 media files belonging to the other 32 guides are byte-identical to the previous revision.


## Community, discovery and short photo-video revision

- Removed the numeric homepage claim and the dedicated Make Together banner, navigation and discovery tab. Existing mixed-age saved projects retain their original data and can still be opened. Seasonal cartoon friends now appear around the homepage, signup, footer, surprise picker and gallery empty states.
- Surprise me filters the active catalogue by season and age, excludes archived guides and avoids immediate repeats when another choice exists. All 15 combinations and single/empty-choice handling pass deterministic checks.
- Added per-activity public galleries with explicit upload consent, adult-account ownership, a separate My projects gallery shelf, withdrawal, resharing, deletion and reporting. Existing private project photos are never auto-published. Names, emails, owner IDs and storage keys are excluded from public responses.
- Appended schema-only migration 0001 for creations and reports; historical migrations are unchanged. Account deletion removes both kinds of photo. Public requests cannot retrieve private or reported images, including by a known ID.
- All 134 route checks pass against isolated SQLite and an object-bucket substitute, including privacy transitions, report enforcement, cross-account denial, upload validation, quotas, failure cleanup, cursor pagination and account deletion. TypeScript and content checks pass. Production authentication/upload transport still requires a signed-in adult; tests do not impersonate a live visitor or publish test images to the real gallery.

- Browser preview confirms the homepage has no “15” claim or Make Together navigation/banner, signup shows the restored cartoon friends, and the new community area loads its honest empty state. Selecting Winter + Little Makers in Surprise me opens WIN-06 with the younger pathway. The new snowman video jumped to step 3 at 30 seconds and played with a full 0–75-second seek range and no media error.
- All 15 active videos are exactly 75 seconds with seven chapters and 15 caption cues; all 35 media sets pass checks. The 60 archived media files and 20 archived metadata records remain byte-identical. Generated photo steps were inspected for coherent progression and captions for readability.
