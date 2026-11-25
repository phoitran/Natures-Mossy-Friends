# Natures Mossy Friends — Product Requirements Document

**Product owner / student:** Harli Cameron  
**Course context:** ENTI 333, Fall 2026 — Lab 4  
**PRD version:** 2.1 — Updated November 23, 2026 (publication status reconfirmed; course crosswalk, competitor evidence, business tests and Replit migration plan reviewed)  
**Product stage:** Published working prototype; practical activity validation and several operational launch requirements remain open.  
**Current site:** https://natures-mossy-friends.natalieforstbauer.chatgpt.site/  
**Implementation baseline:** Published site version 21; source commit `68ddd584154fa7324ea6554da003131b37a6cf59`.  
**Deliverable:** Single Markdown product specification and implementation handoff.

**Update record:** Preserves the attached v2.1 structure, catalogue, FR-01–FR-28 and privacy appendix. Confirms that the site remains at version 21; corrects the Replit authentication options, removes unsupported competitor feature-gap claims, distinguishes documented overlap from positioning hypotheses, and adds clearer migration and commercial-validation gates. This is a document update; it does not change the live site.

## 0. Reader guide and Lab 4 criteria crosswalk

**Product summary:** Natures Mossy Friends is a free-to-explore website that helps parents, guardians and educators of children aged 4–12 pick a seasonal nature craft (leaves, twigs, stones, mud, flowers, sand, snow), see finished examples, and follow five illustrated steps with age-appropriate tasks for two age bands. Adults can optionally create an account to sync projects, keep private photos and share completed creations publicly. A working prototype (site version 21) is already published; this PRD specifies the product, records what is and is not verified, and defines the remaining work to make it a launchable, independently hosted product.

**How to read this document:** Sections 1–3 define the product and its status. Sections 4 and 16–18 cover the problem, market, competitors and business model. Sections 5–10 and 12 are the build specification (catalogue, journeys, numbered requirements FR-01 to FR-28 with acceptance criteria, visual rules, architecture, acceptance gates). Sections 11 and 19 cover hosting and Replit compatibility. Section 20 lists risks; Section 21 is a glossary. Every requirement has a stable ID and an implementation status; separate acceptance evidence distinguishes shipped controls from verified end-to-end outcomes.

### Lab 4 criteria crosswalk

The course requirements recorded in the supplied PRD call for one clearly explained idea, a feasible Replit build, business reasoning, relevant domain familiarity and a single Markdown file. The crosswalk shows where those topics are addressed; it is not a grading decision. Confirm the current assignment wording and any build-platform requirement with the actual handout before submission.

| Lab 4 criterion | Where addressed | Honest status |
| --- | --- | --- |
| Single, clearly explained idea | §0 summary, §1 product decision, §2 changes, §21 glossary | Addressed in this document |
| Buildable and publishable on Replit | §10 architecture, §19 Replit compatibility and build plan | Working prototype exists on another host; Replit mapping is a proposed analysis, not yet performed |
| Makes business sense (market, competitors, model, demand evidence) | §4 problem and validation, §16 niche rationale, §17 competitive landscape, §18 business model | Qualitative analysis; no measured demand or revenue is claimed |
| Owner is familiar with the domain / has connections | §4 owner familiarity and validation access | Owner interest stated; educator and caregiver validation pending |
| Optional: niche supported by AI-assisted development | §16 niche rationale | Feasibility rationale stated; cost advantage unmeasured |
| Single readable Markdown file | Whole document: stable IDs, tables, explicit statuses, glossary | Provided |

## 1. Product decision

Natures Mossy Friends helps grown-ups find seasonal nature activities, understand what they need, and guide children through making something imaginative. Children work with leaves, twigs, stones, mud, flowers, sand and snow. The website supports preparation and occasional guidance; the activity happens away from the screen.

The experience is free to explore. Guests can browse every activity, see finished examples, follow illustrated instructions, watch short photo guides and save progress in their current browser. Adult accounts add synchronized projects, private project photos and optional public sharing of completed creations.

**Core promise:** Find a suitable activity, see what is possible, and start making with clear materials, visual steps and age-appropriate tasks.

**Primary users:** Parents, guardians and caregivers helping children aged 4–12.  
**Secondary users:** Educators, after-school leaders and other adults planning small-group nature activities.  
**Account holder:** An adult. Children are participants, not account holders.

The product's value must come from understandable, achievable activities and a useful repeat experience. More generated imagery alone will not establish demand or prove that a craft works.

### Goals

- Make choosing a seasonal activity quick and welcoming.
- Give younger and older children suitable tasks without making adults interpret a generic tutorial themselves.
- Keep instructions, supplies and examples available without signup or payment.
- Let adults save progress and keep a private record of their creations.
- Enable deliberate, reversible public sharing without exposing account identities.
- Let visitors suggest activities or report problems without leaving their current page.
- Introduce the selected Shelley voice gradually within the approved free-credit approach.
- Enable ordinary email signup without requiring a ChatGPT account in the future independent release.

### Outside the current scope

Paid memberships, checkout, native mobile apps, child profiles, direct messaging, public account profiles, comments and likes, live AI-generated craft instructions, automatic plant identification, location tracking, and full offline synchronization are not current requirements. A clone of the owner's voice is not in use. The selected narration is an existing ElevenLabs library voice.

## 2. What changed from PRD 1.3

| Earlier assumption | Current decision |
| --- | --- |
| The product would be built and published on Replit. | A working site is published on ChatGPT Sites. The current implementation and the independent-hosting work are documented separately. |
| Launch required five activities in every season and a fixed total of 20. | The current curated catalogue is the baseline. No fixed total belongs in hero or promotional copy. Any collection count must come from active records. |
| Make Together was the central discovery feature and navigation destination. | The dedicated section, banner and navigation were removed at the owner's request. Existing mixed-age saved projects remain supported. |
| Every uploaded project photo would remain private. | Private project photos remain private. A separate, explicit action shares a completed creation in that activity's public gallery. |
| Tutorials were longer illustrated videos. | Active tutorials are 75-second photo-step videos, within the requested 60–90-second range, with captions and background music. |
| Decorative movement was unnecessary. | Gentle butterflies, cartoon friends, subtle motion and a cover that advances every four seconds with a smooth crossfade are part of the approved visual direction. |
| Broad pink or pastel blue accents were the theme. | Cream, forest green and muted sage form the main palette. Dusty rose accents and pink butterflies remain; blue is restrained and seasonal. |
| Email/password signup was an assumed launch capability. | The live site uses ChatGPT identity. Independent email/password authentication is prepared in source but not connected or deployed. |
| Read-aloud used the device voice throughout. | A summer nature mandala now uses Shelley recordings. Other activities retain the device voice where supported. |

This revision supersedes the old catalogue, Make Together launch requirements, Replit stack assumption and private-only gallery specification. Earlier versions remain historical planning documents, not descriptions of the published product.

## 3. Status and evidence

**Published** means included in the version 21 source and deployed site. Publication metadata was reconfirmed on November 23, 2026; no newer site release was reported. It does not by itself establish hands-on craft validation, live email delivery or every account workflow. **Prepared** means implementation exists but external setup or deployment is incomplete. **Pending** means the requirement still needs a decision, implementation or acceptance evidence.

| Area | Current status | Important boundary |
| --- | --- | --- |
| Seasonal discovery and age filtering | Published | Filters use active catalogue records; archived records remain for saved-project continuity. |
| Surprise me | Published | Filters season and age, avoids immediate repeats when another result exists, and handles no matches. |
| Activity guides and finished examples | Published | Guides are marked draft; examples are generated inspiration, not proof of physical testing. |
| Short photo tutorials | Published | Active videos are 75 seconds. Photo-style images are AI-generated; these are not live-action demonstrations. |
| My projects | Published | Guest saving is device/browser-specific. Account synchronization uses the live identity service. |
| Private photos and public galleries | Published implementation | Source and recorded isolated tests cover access rules; a complete real-account upload/withdrawal/deletion exercise remains to be documented. |
| Lower-right feedback form | Published interface and integration | Receipt at the requested iCloud inbox is unconfirmed; activation was not found and normal inbox receipt was not tested. |
| Email signup independent of ChatGPT | Prepared | Firebase/standalone code exists, but owner services are not connected and the independent deployment is not live. |
| Shelley narration | Published for A summer nature mandala | All five steps have little, young and legacy together recordings. Other activities fall back to device speech. |
| Visual refinements and new URL | Published | Current URL is above. No independent domain is recorded as configured. |
| Physical activity trials and customer validation | Pending | No completed craft trials, formal customer study or validated revenue are claimed. |

## 4. Audience, problem and validation

A grown-up may find a beautiful craft online but still need to work out whether it suits the children, which materials it needs, how long it takes and what the child can do independently. A finished image can conceal a difficult join or unrealistic construction.

The hypothesis is that a focused, approachable collection with clear steps will reduce this preparation burden and encourage repeat use. Familiar substitutes include search engines, craft videos, saved social posts and printable activity resources. The product must outperform the family's existing method on clarity and usefulness, rather than merely add another place to browse.

Harli's interest in making and experience coordinating materials and customer work support product discovery and give the owner a working familiarity with the problem domain. They do not substitute for an educator's review or practical trials of activities with the intended age group. Recruitment is intended through the owner’s caregiver and educator networks. No participant commitments, completed interviews or formal partnerships are recorded.

### Proposed pilot — not completed research

Interview five caregivers and three educators about a recent activity they actually ran. Then observe ten households using a small set of reviewed activities, including both age bands. Collect feedback from adults without child names or identifiable images.

| Question | Initial decision target | Measurement |
| --- | --- | --- |
| Can adults find a suitable activity? | At least 8 of 10 households within two minutes | Observe selection without researcher assistance. |
| Are the directions usable? | At least 7 of 10 complete without instruction-related rescue | Intended grown-up help is allowed; record every confusing step. |
| Is saving understandable? | At least 8 of 10 correctly explain where their project is saved | Test guest and account scenarios separately. |
| Is public sharing understood? | Every participant in the sharing test can distinguish private and public photos before submitting | Stop and revise the flow if the distinction is unclear. |
| Do people return? | At least 5 of 10 independently start a second activity within 14 days | Record reminders separately; a reminder-driven visit is not independent return. |
| Does feedback actually arrive? | Every controlled delivery test arrives once, with the right content | Match the on-page result to inbox receipt. |

These are proposed small-pilot thresholds, not measured outcomes or market estimates. An analytics dashboard is not currently implemented; use consented observations and a simple adult follow-up process first.

## 5. Current activity catalogue

The following names and age eligibility come from the active source catalogue. Times are displayed making-time estimates; preparation and any waiting are described separately. They are not measured trial results.

| Season | Stable ID | Activity | Ages | Making estimate |
| --- | --- | --- | --- | --- |
| Spring | SPR-06 | Meet the mud creatures | 4–12 | 30 min |
| Spring | SPR-07 | Dandelion Crown | 7–12 | 40 min |
| Spring | SPR-08 | Muddy Faces | 4–12 | 25 min |
| Spring | SPR-09 | Spring Fairy Garden | 7–12 | 50 min |
| Summer | SUM-06 | A summer nature mandala | 4–12 | 30 min |
| Summer | SUM-07 | Rocky friends | 4–12 | 25 min |
| Summer | SUM-08 | Our wilderness creatures | 7–12 | 40 min |
| Summer | SUM-09 | Sandy Explorer | 4–12 | 35 min |
| Fall | FAL-06 | Make a Leafy Friend | 4–12 | 25 min |
| Fall | FAL-07 | Fall Fairy Garden | 7–12 | 50 min |
| Fall | FAL-08 | Fall Mandalas | 4–12 | 30 min |
| Fall | FAL-09 | Meet your fall friends | 7–12 | 40 min |
| Winter | WIN-06 | Make a little snow man | 4–12 | 25 min |
| Winter | WIN-07 | A pocket-sized snow village | 7–12 | 40 min |
| Winter | WIN-08 | Snowy Friends | 7–12 | 40 min |

**Age model:** Little Makers = ages 4–6; Young Creators = ages 7–12. Eligibility changes the available activities, and eligible activities include distinct younger/older maker tasks. It does not currently mean every age option has a completely different set of photographs or a separate full tutorial.

Every active activity has five instruction steps. Most have three finished examples; Snowy Friends has six. Older catalogue records are archived rather than removed so previous saved projects can retain their identity and instructions. Archived activities must stay out of ordinary discovery, Surprise me and the homepage rotation.

The current winter collection depends on snow. The earlier requirement for two no-snow winter activities is not fulfilled by this catalogue and is no longer claimed as a shipped feature. A reviewed no-snow alternative is a possible later addition.

### Content-specific requirements already agreed

- **Summer mandala:** Varied leaf, flower and stone circles; simple, handmade patterns rather than uniformly polished designs.
- **Rocky friends:** Flat, loose stone creatures such as turtles, frogs and dragonflies. Do not imply that difficult unsupported upright balancing is the basic activity.
- **Our wilderness creatures:** Older-child activity using bark, twigs, leaves, stones and optional already-detached moss. Encourage invented creatures; do not strip living moss or bark.
- **Sandy Explorer:** A maze or winding route with an entrance, low sand walls, shells and pebbles; optional flowers and shallow water sections. Explain that water can soak into the sand.
- **Leafy owl:** Pebble eyes, not paper eyes.
- **Snowman:** Preserve the pine-cone-hat, classic carrot-nose and upside-down-boots examples inspired by the owner's references.
- **Snow village:** Preserve the original twig-roof cottage example; retain rounded sprig-topped snow houses with twig paths and a distinct snow-block village. Generated reference-inspired scenes are not the original uploaded photographs.
- **Snowy Friends:** Include mice, rabbits, cat with mouse, seated cat, bear and turtle. The mouse has pebble ears. Keep construction and required adult help consistent with the illustrated variation.

## 6. Main journeys

### Find and make

1. Open Home and select a season, Find your next activity, or Surprise me.
2. Choose an age band and any relevant discovery filters.
3. Open an activity and inspect its finished examples, difficulty, supplies, preparation and adult-help notes.
4. Read the guide without registering. Start a project when ready to save progress.
5. Follow the five steps with diagrams, optional read-aloud and the short photo video. Pause media whenever needed.
6. Continue later from My projects, mark the project finished, or remove an unwanted saved project.

### Keep a private memory

An adult account holder opens a saved project and adds a photo of the creation. The photo remains attached to that private project. Downloading or removing it does not change the public editorial examples.

### Share a completed creation

An adult opens an activity's Community creations area, selects a photo, previews it and explicitly confirms public sharing. The photo appears in that activity's gallery without the account name or email. The adult manages visibility and deletion from Your gallery shelf in My projects. Existing private photos are never automatically published.

### Send an idea or report a problem

A visitor opens Ideas & feedback in the lower-right corner, chooses a category, enters a message and optionally supplies a reply address. The form submits without navigating away or opening an email application. Success and failure appear inside the form; failures retain the message.

### Create an account

**Today:** The live site uses Continue with ChatGPT. The displayed email comes from that authenticated identity and cannot be edited inside the site's profile form.

**Required independent experience:** An adult enters their own email and password, confirms the adult-account and privacy acknowledgements, verifies their email, and returns to the activity or My projects. They must not need a ChatGPT account. Password reset, sign-out, error handling and deletion must work on the final production host.

## 7. Functional requirements and acceptance criteria

These IDs replace the previous FR numbering. Status is explicit so an implementation handoff does not mistake desired behaviour for completed work.

### Discovery and homepage

| ID | Requirement | Acceptance criteria | Status |
| --- | --- | --- | --- |
| FR-01 | Free guest exploration | All active activities, materials, written steps and examples open without account creation or payment. | Published |
| FR-02 | Four seasonal collections | Spring, Summer, Fall and Winter remain visible and labelled. Season filter pills use their assigned colours. Counts derive from active data. | Published |
| FR-03 | Age and catalogue filters | Little Makers and Young Creators show eligible activities. Search, making-time and material filters operate on the active collection. No-match states allow explicit changes. | Published |
| FR-04 | Surprise me | Apply selected season and age before choosing. Exclude archives, avoid the last selection if alternatives exist, and disable selection when empty. | Published |
| FR-05 | Rotating cover | Rotate through every active activity every four seconds, with a smooth crossfade. Pause/Play sits below the image by its green frame. Reduced-motion preference disables automatic movement; hidden tabs do not advance the cover. | Published |
| FR-06 | Retired Make Together discovery | No dedicated Make Together banner, navigation tab or primary section. Preserve older mixed-age project records and their instructions. | Published |
| FR-07 | Accurate marketing copy | Do not reinstate “15 seasonal projects,” “15 little adventures,” or another hardcoded catalogue total in promotional text. | Published requirement |

Material filtering currently checks named required natural-material categories; it is not a complete suitability assessment. The app does not currently collect live weather, inventory quantities, tool permissions or adult staffing and must not imply that it has checked them. Time filtering uses the making-time field, not a validated total elapsed session duration. A richer rules engine would be a separate enhancement.

### Activity instructions and media

| ID | Requirement | Acceptance criteria | Status |
| --- | --- | --- | --- |
| FR-08 | Preview the outcome | Show a finished-result image before starting, plus labelled alternative examples. Keep generated inspiration distinguishable from community submissions. | Published |
| FR-09 | Complete step guidance | Display all step titles, the current numbered step, its diagram, written action, age-specific task and applicable grown-up help. Next/Previous and direct step selection show the matching content. | Published |
| FR-10 | Clear start and resume | Starting opens the instructions and creates a saved project; returning continues existing progress. Merely viewing an activity must not create a new project. | Published |
| FR-11 | Readability and print | Provide larger text, diagram enlargement and a print guide. Instructions remain usable if media or speech fails. Verify keyboard focus and phone layouts during release QA. | Published controls; broader audit pending |
| FR-12 | Short realistic photo guide | Active videos remain 60–90 seconds, currently 75, with photo-style steps, concise captions, playback controls, chapters and download. Label generated imagery accurately. | Published |
| FR-13 | Shelley step narration | Use the correct recording for activity, step and age option. Stop when the user changes steps, age, route or relevant dialog. Starting video stops narration; starting narration pauses video. | Published for SUM-06 |
| FR-14 | Reliable narration fallback | Use device speech for activities without recordings and when a recording fails. Never play a stale recording after its instruction text changes. Show an honest error if speech is unavailable. | Published |
| FR-15 | Gradual voice rollout | Produce the exact current directions, including grown-up help, in a bounded batch; validate files and playback before publication. Keep the ElevenLabs attribution. No paid upgrade or recurring generation is implied. | First batch complete; remaining activities pending |

Shelley is **“Shelley – Clear, Confident and British”**, voice ID `4CrZuIW9am7gYAxgo2Af`. Version 21 includes 15 MP3 files covering five SUM-06 steps and three role variants, including legacy together support. These are stored assets; visitors do not trigger new speech-generation charges. The last generation session recorded 4,281 free credits remaining; this is a dated observation, not a guaranteed current balance.

The short videos still have captions and instrumental music with **no spoken narration**. Shelley is attached to Read this step aloud. Adding narration to the videos would be separate work. Free-plan narration was published with an ElevenLabs credit; recheck usage rights before commercial use or a change in licensing.

### Projects, photos and community

| ID | Requirement | Acceptance criteria | Status |
| --- | --- | --- | --- |
| FR-16 | My projects | Show in-progress, finished and saved-for-later items. Guests retain progress in this browser; signed-in users use account storage. State the save destination honestly. | Published |
| FR-17 | Data transfer and removal | Preview guest-to-account transfer and JSON backup import. Export/import progress and favourites; state that photos are separate. Removing a project leaves the catalogue activity available. | Published |
| FR-18 | Private project photos | Adults can add up to three photos per saved project, download them and remove them. Another account and a signed-out visitor cannot retrieve them. | Published; live transport acceptance pending |
| FR-19 | Public activity gallery | Each activity has a Community creations area and explicit public-upload confirmation. Account names, emails, owner IDs and object-storage keys are not exposed in gallery responses. | Published; live upload acceptance pending |
| FR-20 | Visibility and deletion | Owners can make their gallery images private, explicitly reshare eligible private images, or delete them. Private project photos and public-gallery records remain separate. | Published |
| FR-21 | Reporting | A signed-in adult can report another public photo for privacy, inappropriate content or not being a project. Reporting hides it; owner controls cannot republish a reported image. | Published controls; operational review process pending |
| FR-22 | Image validation | Accept JPG, PNG or WebP within the input limits; process to a display JPEG and strip embedded metadata. Reject invalid uploads and enforce ownership and quotas server-side. | Published implementation |

Current limits: up to 10 MB and 25 megapixels at selection, maximum 2,048 pixels on the processed image's longest side, three private photos per project, six gallery photos per activity per account, 60 gallery photos per account, and a combined 150 MiB processed-photo quota per account. HEIC requires a JPEG export first. Browser re-encoding performs image conversion; server code validates the resulting JPEG, dimensions and blocked metadata markers. Do not describe this as a full server-side image-decoding or visual content-moderation service.

Public photos can be copied by visitors. Withdrawing or deleting a photo stops access through the app; it cannot recall copies already downloaded. Initial public submissions are not pre-approved by an editorial moderator. Automated detection of faces or identifying details is not implemented. The product therefore needs a clear operational owner for reports and privacy requests before a wider community launch.

### Accounts and feedback

| ID | Requirement | Acceptance criteria | Status |
| --- | --- | --- | --- |
| FR-23 | Truthful current signup | Explain that the live identity comes from ChatGPT. Do not present a locked account email as a normal editable email signup field. | Published |
| FR-24 | Independent email accounts | A new adult registers with their own email, verifies it, signs in and resets a password without a ChatGPT account. Complete this on the chosen production host. | Prepared; not deployed |
| FR-25 | Privacy acknowledgement | Show a concise explanation and the full policy in a scrollable signup dialog; require adult and policy confirmation. The permanent privacy page uses the same policy source. | Published |
| FR-26 | Account deletion | Remove the adult's profile, favourites, progress, private photos and gallery creations. Explain that deleting this site's account does not delete a ChatGPT account. For standalone auth, coordinate identity deletion and retry failures. | Published code; live acceptance pending |
| FR-27 | Feedback without navigation | Lower-right Ideas & feedback opens on the current page. Offer activity idea, requested change, problem and other feedback; optional reply email; preserve failed messages. | Published |
| FR-28 | Confirmed feedback delivery | Send to naturesmossyfriends@icloud.com. Test normal inbox receipt, provider activation, successful receipt and failure states. Do not mark delivery accepted merely because the local endpoint responds. | Integration published; delivery unconfirmed |

Feedback messages are limited to 2,000 characters. The server validates and throttles requests, then the browser sends through FormSubmit. The current app does not maintain a durable feedback inbox or retry queue. FormSubmit acceptance is not proof that a message reached the owner's mailbox. The requested feedback address is iCloud; footer Say hello and the privacy contact currently use **naturesmossyfriends@gmail.com**. Confirm whether both addresses are intentional and monitored before changing them.

## 8. Visual and interaction direction

The site should feel like a gentle, colourful nature-making space, with enough movement to feel alive and enough restraint to keep instructions easy to follow.

| Element | Current direction |
| --- | --- |
| Main canvas | Warm cream, `#fcfbf5` |
| Main headings and primary actions | Forest green, `#245a3d` |
| Supporting surfaces, top strip and footer | Muted sage; softly translucent where appropriate |
| Small flower/leaf accents and logo star | Dusty rose, including `#b88493`; related soft rose fills |
| Butterflies | Retain pink; restrained blue-grey and warm gold companions where already used |
| Spring filters | Pale leafy greens |
| Summer filters | Soft warm yellows |
| Fall filters | Peach, warm orange and muted autumn tones |
| Winter filters | Soft icy blue; not a dominant sitewide blue treatment |
| Decorative style | Cute cartoon nature friends and sparse fluttering butterflies around Home, discovery, signup and My projects |
| Activity imagery | Handmade, irregular and achievable; clearly labelled generated inspiration where applicable |

Keep the approved copy: **“Small hands. Wild imaginations.”**, **“A little World Made By Little Hands”**, **“Big ideas. Small beginnings.”**, and **“Little adventures. Always free to explore.”**

Butterflies must remain behind content, ignore pointer input and never obstruct controls. Reduce decoration on small screens. Honour reduced-motion settings for butterflies, hover effects and the cover. Preserve a visible selected filter state beyond colour alone. Maintain readable contrast, labelled controls, focus visibility, sensible reading order and no horizontal page overflow at 360px.

The four-second timing applies to the cover's next activity, not the entire cycle. It rotates one cover view from every active activity, not every example photograph within each gallery.

## 9. Content quality and release rules

The current guides are draft content. Generated examples can illustrate possibilities but cannot establish age suitability, construction stability or real completion time.

Before describing an activity as tested:

1. Make its basic version using the listed materials and instructions.
2. Check the younger/older tasks, adult-help steps and more complex pictured variations.
3. Record preparation, making, waiting and cleanup times and any failed steps.
4. Photograph an actual result and, where useful, difficult intermediate steps.
5. Have an appropriate educator or experienced nature-activity facilitator review the guide.
6. Correct the written steps, diagrams, photos, video captions and recorded narration together.
7. Record reviewer, trial date, content version and remaining limits.

Use already-loose natural materials where collecting is allowed. Keep material identification and flower-picking decisions with the grown-up. Instructions must explain cleanup, removable decorations, temporary outdoor work and any conditions such as packable snow. Do not infer safe materials from an image or claim numerical environmental savings.

Snow structures remain miniature craft models, not shelters for children to enter. Images must show plausible joins and natural materials consistent with the instructions. Generated inspiration must never be inserted into the public gallery as if a family submitted it.

## 10. Current technical architecture

| Layer | Current implementation |
| --- | --- |
| Frontend | React and TypeScript with Vinext/Vite and app-router-style pages |
| Published host | ChatGPT Sites; server build targets a Cloudflare Worker |
| Current identity | ChatGPT identity supplied through the Sites authentication flow |
| Structured account data | D1 database |
| Uploaded photos | R2 object storage behind application access checks |
| Guest progress and favourites | Versioned browser localStorage |
| Catalogue and policy | Version-controlled JSON |
| Editorial media | Stored diagrams, gallery images, MP4s, VTT captions, posters and MP3 narration assets |
| Feedback | Same-origin validation/throttle endpoint plus browser-side FormSubmit delivery |
| Prepared independent deployment | Separate Worker entrypoint and Firebase email/password authentication; not configured or published |

The current app is not a static HTML folder that can be moved unchanged to any web host. Accounts, uploads, galleries and feedback depend on server behaviour and storage bindings. An independent move must either support the current backend or include an explicit backend migration.

### Key routes and source locations

| Surface | Route or source |
| --- | --- |
| Home | `/` |
| Catalogue | `/activities` |
| Activity | `/activities/{id}` |
| Personal shelf | `/my-projects` |
| About | `/about` |
| Account and privacy | `/account`, `/privacy` |
| APIs | `/api/account`, `/api/auth`, `/api/projects`, `/api/photos`, `/api/creations`, `/api/feedback` |
| Activity records | `content/activities.json` |
| Policy source | `content/privacy.json` |
| Video and narration manifests | `content/videos.json`, `content/short-video-captions.json`, `content/narration.json` |
| Narration matching | `lib/step-narration.ts` |
| Independent deployment notes | `docs/independent-hosting.md` |

### Data model

| Record | Purpose |
| --- | --- |
| Activity | Stable ID, season, age eligibility, making/prep time, materials, roles, steps, examples, review status and archive state |
| Account | Provider identity, email, optional name, policy version and storage accounting |
| Saved project | Owner, activity, role variant, current step, progress state and update time |
| Favourite | Owner and activity, separate from project progress |
| Private photo | Owner, saved project, object key, file size and created time |
| Gallery creation | Owner, activity, object key, size, created time and public/private/hidden state |
| Creation report | Reporter, creation, selected reason and time |
| Auth/feedback throttle record | Limited-lived request-count data |
| Narration record | Activity, step, role variant, exact spoken text, asset path, voice/provider and generation date |

The richer old design for a full material-substitution engine, per-child quantity model, revision-conflict UI and tracked deletion-job queue is not verified as implemented. Those are possible future requirements, not capabilities to promise in the current product.

## 11. Independent signup and hosting plan

The owner wants account signup without ChatGPT. That requirement is still open despite a working public site.

Prepared source includes a separate Firebase email/password mode, email verification, password recovery, secure session handling, provider checks and a standalone build. No connected Firebase project or independent production host is recorded as live. A new address alone will not complete this requirement.

**Decision sequence:**

1. Confirm the owner-controlled host and repository account. Cloudflare/Firebase is the prepared technical path; Exclusive Hosting has also been discussed, but compatibility and backend adaptation are unresolved.
2. Confirm costs and limits before accepting paid services. Do not describe account storage or email infrastructure as guaranteed free forever.
3. Configure production auth, verification/reset messages, database, private object storage and a working privacy contact.
4. Test registration with a genuinely new email, verification, password recovery, sign-out, private access, public sharing and deletion on the chosen host.
5. Plan migration of existing user data and the final URL; preserve the old site until the new one passes acceptance.

Guest data is origin-specific. Current progress exports can help move favourites and project records, but photo files are separate and public sharing must be chosen again. Never link old and new accounts merely because an unverified submitted email matches. A bulk account/photo migration, custom domain and automatic cross-host synchronization have not been completed.

## 12. Operational priorities and acceptance gates

| Priority | Work | Completion evidence |
| --- | --- | --- |
| P0 for independent-account launch | Decide hosting and finish email signup | A new adult signs up without ChatGPT; verification and reset arrive; account data works across devices and remains isolated. |
| P0 for feedback promise | Confirm the iCloud inbox and FormSubmit delivery | A controlled form submission stays on-page and arrives exactly once; activation and failure paths are documented. |
| P0 before calling content tested | Trial and review a small set of representative activities | Recorded trials, actual photographs, corrected instructions and named reviewer/date. |
| P1 before wider public sharing | Complete real-account gallery and private-photo acceptance; assign a moderation owner | Two-account access tests, upload/withdraw/report/delete results, and a documented report-handling procedure. |
| P1 | Confirm privacy/support contacts and retention process | Both configured addresses are intentional and monitored; policy and actual providers/cleanup agree. |
| P1, gradual | Extend Shelley narration in small batches | Exact instruction text, validated files, attribution, playback checks and budget/credit check for each batch. |
| P1 | Accessibility and performance review on real devices | Keyboard-only completion, mobile layout, reduced motion, text enlargement, captions, media failures and measured load results. |
| P2 | Improve discovery and measured content quality | Trial-based time estimates, better material matching, no-snow options and changes driven by adult feedback. |

Do not replace these gates with a single “website works” checkbox. Publication, authenticated access, email receipt, craft completion and demand are separate questions.

### Acceptance scenarios

- Spring + Little Makers shows only eligible current spring activities; changing age updates the actual results.
- Winter + Little Makers in Surprise me opens the little snowman, with the younger task. Archived records never appear.
- The cover includes every active activity, changes after four seconds and stops when paused or reduced motion is enabled.
- A guest starts, advances and reloads a project; progress remains in that browser. A second device does not falsely show it as synchronized.
- A saved private photo cannot be loaded by another adult or by an unauthenticated request.
- A public upload requires explicit confirmation; the public response omits account identity; making it private revokes public retrieval.
- A reported creation disappears and cannot be republished through the owner's visibility controls.
- Removing a saved project deletes its linked private data but does not delete separate gallery uploads; account deletion removes both photo categories.
- Invalid, oversized and unsupported image files fail clearly without consuming orphaned storage quota.
- Feedback failure leaves the message intact. A success test is matched to actual inbox receipt.
- SUM-06 plays Shelley for the chosen step and age. Navigation stops audio, and a changed instruction cannot select an outdated recording.
- Other activities keep usable text and diagrams even when the browser has no speech voice or video cannot load.
- Independent signup passes with an email that has no ChatGPT account before it is announced as available.

### Evidence already recorded

The repository contains content, discovery, route, auth, feedback, media and narration checks. Earlier QA notes document isolated ownership/privacy tests and representative browser checks. The version 21 update passed TypeScript, production build and narration file/text checks. Live browser playback of the published SUM-06 narration was verified in the preceding delivery, including stop behaviour; preview checks covered step/age changes and audio/video handoff.

The implementation baseline comes from the earlier version 21 source review and recorded checks. This update rechecked publication metadata and reviewed the attached document against that baseline; it did not rerun a full regression suite, submit a public test photo, send feedback or establish real craft outcomes. Older QA entries mentioning longer videos or Make Together navigation describe earlier revisions; the current specification above takes precedence.

## 13. Business model and measurement

The current offer is free. There is no implemented checkout, subscription, advertising revenue model or confirmed willingness to pay. Keep access to existing basic activities and instructions free.

The earlier CAD $9.99 pack proposal and operating-cost calculations were hypotheses tied to a different scope. They are not approved pricing, a current vendor quote or a validated budget. Optional paid extensions can be reconsidered after repeat use and content quality are established, with a fresh cost model and media-licensing review.

Track actual hosting/storage use, email delivery, content production, activity-review time, moderation effort and narration credits. Pre-generated media avoids per-visitor generation, but storage, bandwidth and maintenance still need an owner. No purchase, subscription or recurring generation schedule is authorized by this document.

Useful future measures are activity selection time, starts, completions, second-activity use, failed saves/uploads, feedback delivery failures and report resolution. Define an observation or analytics method and appropriate privacy choices before presenting numbers. A completion click alone is not proof that a child completed the physical project.

## 14. Course and development handoff

The course requirement recorded in the supplied PRD is a single Markdown PRD for an idea that can be built and published on Replit. This product is currently built and hosted through ChatGPT Sites. Section 19 analyses how each component maps to Replit and gives a milestone plan, but no Replit deployment exists. Do not claim a working Replit build without a Replit deployment, or that this meets a Replit-specific course requirement without instructor acceptance.

For a handoff, provide the current source repository, setup/build instructions, content inventory, asset provenance, test commands, environment-variable names without secret values, known gaps and deployment/migration plan. Keep personal accounts, uploaded user photos and credentials out of a public repository. Choose the owner's intended GitHub account before creating a new repository; no account ownership is assumed from this PRD.

A useful demonstration shows a seasonal filter, Surprise me, one complete guide, the 75-second photo video, Shelley read-aloud on the summer mandala, guest project resumption, and the private/public photo distinction. Describe independent signup and unresolved feedback delivery as pending. Do not show a simulated email or upload as if it succeeded in production.

## 15. Source of truth and revision control

The attached v2.1 document is the editing baseline. Publication metadata confirms that site version 21 remains current; implementation details are retained from the earlier review of the identified version 21 source, including the catalogue, API handlers, media manifests and hosting notes. Product decisions come from the owner’s requests. The earlier PRD supplies historical course and discovery context; the current assignment handout remains authoritative for assessment requirements.

Useful handoff records:

- Live site: https://natures-mossy-friends.natalieforstbauer.chatgpt.site/
- Narrated example: https://natures-mossy-friends.natalieforstbauer.chatgpt.site/activities/SUM-06
- Selected voice: https://elevenlabs.io/voices/4CrZuIW9am7gYAxgo2Af
- Source QA history: `docs/QA.md`
- Content review notes: `docs/content-review.md`
- Narration coverage and production notes: `docs/narration.md`
- Independent-hosting preparation: `docs/independent-hosting.md`

Sections 17 and 19 use current first-party pages reviewed on November 23, 2026. No traffic, revenue, vendor-price estimate or legal-compliance claim is inferred from those pages. Source descriptions and product hypotheses are labelled separately. Before changing host, signup provider, public-sharing behaviour, feedback recipient or commercial use, update the affected requirements and operational acceptance evidence together.

## 16. Niche rationale

The initial niche is adults helping children aged 4–12 make small seasonal projects from available natural materials. The scope combines age-banded tasks, visual instructions, short photo guides, saved progress and optional sharing. Purchased craft kits are not required, although individual activities can still need basic household supplies.

AI-assisted coding and pre-generated media have helped produce this prototype. They may lower the initial cost of a specialized product, but no comparison with conventional development costs has been measured. They do not remove activity trials, image review, software verification, accessibility, moderation or ongoing support.

The business rationale is therefore a hypothesis: a small owner-operated product might serve this audience at a manageable cost if families return and maintenance stays affordable. A narrow niche is useful only if it solves a recurring problem. The pilot in §4 should test that before catalogue expansion or paid features.

## 17. Competitive landscape

First-party pages were reviewed on November 23, 2026. The observations below establish competing content and delivery approaches; they do not establish competitors’ full feature sets, quality, traffic or revenue. The final column contains questions to test, not proven market gaps.

| Alternative | Observed overlap | Implication and comparison to test |
| --- | --- | --- |
| [Nature Play WA — Nature Craft Ideas](https://www.natureplaywa.org.au/category/families/nature-play-ideas/nature-craft-ideas/) | Offers natural-material craft ideas, including stick stars, leaf gift tags and tree weaving, plus a separate activity-card product. | Nature crafts and portable prompts already exist. Test whether the app’s age tasks, saved progress and media make a comparable session easier to prepare. |
| [Garfield Park Conservatory — At-home Nature Play](https://garfieldconservatory.org/resource-center/at-home-nature-play-activities/) | Groups downloadable activities into summer, fall, winter and spring; includes leaf rubbings, nature mandalas and other family activities. | Seasonal organization is not unique to this product. Compare a downloaded activity with the app’s guide on preparation, comprehension and successful completion. |
| [Twinkl Parents — Nature Activities](https://www.twinkl.co.uk/blog/top-ten-nature-activities-for-kids) | Provides family-oriented nature art and craft ideas, instruction resources, scavenger hunts and links to video content. | Do not frame Twinkl as serving only schools or lacking visual guidance. Test whether a focused, no-purchase-required journey helps the intended family more than its existing resource. |
| Parenting/craft blogs | Rainy Day Mum’s nature-activity category was accessible, but its activity details were not exposed in the retrieved page. What Do We Do All Day and How We Learn could not be fully reviewed through the research tool. | Retain these as research leads. Do not assert that they lack saving, age adaptation or another feature without inspecting the relevant experience. |
| Video/social platforms and nature apps | These remain plausible substitutes from the original market analysis; no specific app’s complete workflow was verified in this update. | Ask participants which service they actually use. Benchmark that named workflow instead of assuming a universal feature gap. |

**Positioning to test:** a focused, free-to-explore nature-making experience in which an adult can inspect supplies, adult-help notes, age-banded tasks and examples, follow a guide, and keep progress in one place. This is a proposed convenience benefit, not an exclusive invention or demonstrated competitive advantage.

**Current weakness:** the site’s guides remain draft and its examples are generated inspiration. Established resources may already satisfy the family’s needs. Hands-on trials and actual-result photos in §9 are therefore business priorities as well as content-quality work.

**Comparison method:** During the pilot, compare two similarly demanding activities using the participant’s usual resource and this site; alternate the order. Record selection time, preparation effort, missing supplies, confusing steps, completion and preference. Do not generalize from one weak competitor example or treat a preference as willingness to pay.

## 18. Business model hypotheses

The current offer is free (§13). This section lists options to evaluate later; none is approved, priced or implemented.

| Option | Description | Preconditions | Risk |
| --- | --- | --- | --- |
| Remain free | Portfolio/community product funded within an owner-approved operating budget | Track hosting, storage, delivery services, media production, review, support and moderation (§13) | No revenue; owner must fund ongoing work |
| Optional paid extensions | Additional printable packs or reviewed activities, while existing basic activities and accessibility support stay free | Repeat use, a complete tested offer, explicit commercial rights for all included media and a fresh cost model | Willingness to pay unproven; earlier CAD $9.99 idea is not approved |
| Educator or group offering | Small-group planning tools for after-school leaders | Educator interviews (§4) | Needs features outside current scope |
| Sponsorship or partnership | Local nature organisations, libraries or schools | Moderation and privacy owner in place | Brand and child-safety review burden |

**Unit costs to measure before any pricing decision:** hosting and storage per active account, email delivery, pre-generated media production, activity review time, moderation effort and narration credits. Pre-generated media means visitors cause no per-visit generation cost. **Demand evidence to date:** none measured; the pilot thresholds in §4 are the planned method. **Decision rule:** meeting the 5-of-10 return-use target and having tested content permits a pricing experiment; it does not validate a paid business. Offer one concrete, complete extension at an explicitly stated price to eligible adults and record actual purchases, refunds and reasons for declining. A survey response, waitlist entry or button click is not a sale.

**Economic check before launch:** Define contribution per sale as price received less payment/refund allowance, variable delivery and support costs. Monthly break-even purchases equal recurring operating cost divided by positive contribution per sale, rounded up. Track initial development and new-pack production separately; do not assume a customer repeatedly buys the same one-time pack. No prices, conversion rate or profitable outcome are established here.

## 19. Replit compatibility and build plan

Replit remains a candidate course-build target, not the current production host or an approved purchase. Official documentation supports a possible full-stack route using server deployment, PostgreSQL, App Storage and independent app accounts. These capabilities do not make the existing Cloudflare Worker build directly portable. The mapping below is an engineering proposal; no Replit migration has been implemented or tested.

**Authentication distinction:** Replit Auth uses Replit accounts. It would remove a ChatGPT dependency while introducing another platform-account dependency. For the intended own-email signup experience, evaluate **Clerk Auth** or adapt the prepared Firebase integration. Replit documents Clerk Auth as providing independent app accounts, email/password authentication and email verification. Choosing Clerk would be new integration work; the existing Firebase work is not a Clerk implementation. [R1, R2]

| Current component (§10) | Proposed Replit mapping | Required migration work |
| --- | --- | --- |
| React/TypeScript UI with Vinext/Vite | Reuse UI and content inside a verified Node-compatible frontend/server setup | First prove a minimal build. Adapt Worker imports, build integration, routing and entrypoints; do not expect the current scripts to run unchanged. |
| Server API routes | Node/framework routes preserving the existing API contract | Port ownership checks, validation, quotas, throttling and error handling; rerun route tests. |
| D1 records | PostgreSQL [R3] | Translate SQLite-specific SQL, bindings, migrations and transactional behaviour. Verify ownership references and data counts before migration. |
| R2 photos | App Storage [R4] | Replace storage calls; serve private images only after authorization and public creations only when their state permits it. Bucket privacy alone does not secure an app’s public routes. |
| ChatGPT identity | Clerk Auth or adapted Firebase integration | Create app-owned identities, email verification/reset, sessions, adult/policy acknowledgement and deletion; validate in production as well as development. |
| Guest localStorage | Retain browser-side storage format where compatible | Export/import when origins change; do not promise automatic cross-domain transfer. |
| JSON catalogue, policy and media manifests | Repository files | Keep stable activity IDs and exact-text narration matching. |
| MP4, VTT, MP3 and illustrations | Bundled assets or authenticated/public media delivery as appropriate | Check asset size, content types, caching, video seeking and accessibility on the deployed host. |
| Feedback | Retain FormSubmit or select a separately approved mail service | Revalidate the final origin, spam controls and actual receipt at the iCloud address. |
| Secrets | Environment configuration outside source control | Document names only; replace host-specific bindings and credentials securely. |
| Publication | A server-capable deployment such as Autoscale [R5] | A static-only deployment cannot supply this app’s backend. Confirm costs and production configuration before enabling it. |

### Dependency-ordered milestones

1. **Portability proof:** Build and deploy a guest-only vertical slice containing discovery and SUM-06 with images, captions and narration. Confirm direct URL refresh, asset loading, step selection and no accidental account prompts. This is a migration spike, not a finished full-catalogue launch.
2. **Accounts and data:** Implement the chosen auth provider and PostgreSQL layer. Pass a new-email signup/verification/reset test and two-account isolation tests before enabling real accounts. Preserve FR-16, FR-17 and FR-23–FR-26.
3. **Photos and community:** Port image storage, quotas, consent, visibility, reporting and deletion. Pass FR-18–FR-22 with temporary test accounts and creation-only images.
4. **Feedback and policy:** Verify inbox delivery and update provider/contact information in the shared policy source. Reconcile FR-25, FR-27 and FR-28 with actual behaviour.
5. **Full-content acceptance:** Check every active activity and media reference, preserve archived saved-project access, run the applicable §12 checks and record failures explicitly.
6. **Cutover rehearsal:** Verify source/data backups, account mapping, record counts and photo checksums. Confirm owner access to repository and hosting, demonstrate rollback, then decide whether to change the public URL. Keep the current site available until acceptance is complete.

Estimate effort after the portability proof. The source’s database and storage bindings, identity handling and build integration make a backend migration material work, not a file upload. A Replit course demonstration and a move of the real production site are separate decisions. No deployment, paid plan or data transfer is authorized solely by this PRD.

### Official references — reviewed November 23, 2026

- **R1 — Replit Auth:** https://docs.replit.com/features/auth-and-identity/authentication
- **R2 — Clerk Auth:** https://docs.replit.com/features/auth-and-identity/clerk-auth
- **R3 — Replit Database:** https://docs.replit.com/features/data-and-storage/sql-database
- **R4 — App Storage:** https://docs.replit.com/features/data-and-storage/object-storage
- **R5 — Deployment types:** https://docs.replit.com/features/publishing/deployment-types

Check plan limits and pricing at implementation time. The cited pages support platform capability statements; they do not verify this application’s integration, security, performance or course compliance.

## 20. Risks and mitigations

| Risk | Impact | Mitigation | Owner |
| --- | --- | --- | --- |
| Untested activities fail with real children | Loss of trust, safety concerns | §9 trial and educator review before any "tested" claim | Product owner |
| Public photos expose children or identifying details | Privacy harm | Policy guidance, explicit confirmation, reporting, named moderation owner before wider launch | Product owner |
| Feedback or privacy email goes unseen | Missed reports and requests | P0 delivery test; confirm both addresses are monitored | Product owner |
| Independent signup not delivered | Users still need ChatGPT | §11 decision sequence and acceptance test | Product owner |
| Generated imagery mistaken for real results | Misleading expectations | Keep labelling (FR-08, FR-12); replace with real photos after trials | Product owner |
| Third-party narration licence changes | Commercial-use limits | Recheck ElevenLabs terms before commercial use | Product owner |
| No demonstrated demand | Wasted effort | Run §4 pilot and a separate purchase experiment before investing in paid features | Product owner |
| Report controls are abused or reports are not reviewed | Legitimate creations disappear or privacy issues remain unresolved | Assign a moderator, record handling steps and test report/withdrawal paths before wider sharing | Product owner; delegate before launch |
| Host migration breaks ownership or loses photos | Account data exposed or unavailable | Portability proof, two-account tests, verified backups, explicit identity mapping and rollback before cutover | Product owner and implementation lead |
| Course-platform assumption is wrong | Submission fails a specific requirement | Confirm the handout/instructor requirement before funding a platform migration | Student |

## 21. Glossary

- **Active activity:** a catalogue record shown in discovery, Surprise me and the homepage cover. **Archived activity:** kept only so older saved projects keep their identity and instructions.
- **Little Makers / Young Creators:** age bands 4–6 and 7–12.
- **Guest:** a visitor without an account; progress is saved in that browser only.
- **Private photo:** a photo attached to a saved project, visible only to its owner. **Gallery creation:** a separate uploaded-photo record associated with an activity; it can be public, private or hidden after a report. Public sharing requires confirmation.
- **Shelley:** the ElevenLabs library voice "Shelley – Clear, Confident and British" used for recorded narration (currently only activity SUM-06).
- **Published / Prepared / Pending:** implementation-status terms defined in §3; publication does not imply completed acceptance testing.
- **Replit Auth / Clerk Auth:** the former uses Replit accounts; the latter provides independent app accounts. See §19.
- **Acceptance evidence:** a recorded result from a defined check, such as verified inbox receipt or denial of cross-account photo access.
- **Generated inspiration:** AI-generated example imagery, not a family submission and not proof of a physical trial.

## Appendix A. Current site privacy-policy text

The following is the policy text stored in version 21, included to keep the PRD and current publication aligned. Its displayed dates are preserved. Operational work remains to confirm contacts, actual provider configuration and retention/deletion procedures; this appendix is not a new legal-compliance certification. Standalone mode also displays provider-specific context in the interface.

**Effective date:** November 19, 2026  
**Last updated:** November 22, 2026

### 1. Introduction

Welcome to Natures Mossy Friends.

Natures Mossy Friends is a creative activity platform designed to help parents, guardians, and other grown-ups discover activities, explore ideas, and create meaningful experiences with children. Our goal is to encourage creativity, curiosity, and hands-on play through simple, engaging activities.

We value your privacy and are committed to protecting the personal information you share with us. This Privacy Policy explains what information we collect, how we use it, how it is stored, and the choices you have regarding your personal information when you use our website.

By using Natures Mossy Friends, you acknowledge this Privacy Policy.

### 2. Information We Collect

We collect only the information necessary to provide and improve your experience on Natures Mossy Friends.

**Information you provide**

When you create an account, we collect your email address. You may optionally add your first name and last name to your adult profile. Names are not required to create an account.

Our authentication provider processes your sign-in credentials, email verification and account-recovery information. We do not store plaintext passwords in the Natures Mossy Friends application database.

When you use your account, we may also save information about your activity on the platform, including:

- Activities you save or mark as favourites.
- Projects you choose to save, their progress and completion status.
- Your saved activity and project preferences.
- Optional photographs of finished projects that you choose to keep privately or explicitly share in an activity’s public gallery.
- Photo sharing choices and reports about gallery content.
- Your confirmation that the account is for an adult and the version and time of your Privacy Policy acknowledgement.

We also process limited technical information needed for authentication, essential sessions, error handling and website security. Our service providers may process connection and security information, such as IP addresses and browser information, for those purposes.

You can browse activities and read instructions without an account. If you save progress as a guest, that progress is stored in your browser on the device you are using. It is not added to an account unless you choose to transfer it after signing in.

We do not require you to provide information about children to create an account or use our platform.

### 3. How We Use Your Information

We use the information we collect to:

- Create and manage your account.
- Allow you to sign in and access your saved information.
- Save your favourite activities, projects, progress and preferences across devices when you are signed in.
- Store and display the finished-project photographs you choose to keep privately.
- Publish a finished-project photo in an activity gallery only when you explicitly choose Share publicly.
- Personalize your experience by making previously saved activities accessible to you.
- Maintain, operate, and improve our website.
- Respond to questions, requests, or support inquiries.
- Protect the website against unauthorized access, misuse, or other security concerns.

We do not collect personal information for purposes unrelated to providing and maintaining Natures Mossy Friends. Creating an account does not subscribe you to marketing emails.

Photos attached to your saved projects remain private. A separate Share publicly choice lets you upload a completed-project photo to an activity gallery where anyone can view it. Your account name and email are not displayed with shared photos. We do not automatically publish private photos, use uploaded photos in advertising, or submit them to generative AI services. Authorized service providers process them as necessary to store, secure and display them. Public photos may be copied by others; making a photo private or deleting it cannot recall copies already saved elsewhere.

### 4. Children's Privacy

Natures Mossy Friends is designed for adults to discover, organize, and participate in creative activities with children.

Accounts are intended for parents, guardians, and other adult users. Children should use the platform with the involvement and supervision of an adult and should not independently create accounts or provide personal information through our website.

We do not knowingly request or require children to provide their personal information. We encourage adults to avoid including children's full names, contact information, photographs, or other identifying details in any saved project or information submitted to the platform. When uploading a finished-project photo, photograph the creation itself without children or other identifying details.

If we become aware that personal information belonging to a child has been provided to us without appropriate authorization, we will take reasonable steps to address the information and, where appropriate, delete it.

### 5. How We Share Your Information

We respect your privacy and do not sell or rent your personal information.

We may share limited information with third-party service providers who help us operate Natures Mossy Friends, such as website hosting, account authentication, verification-email delivery, data and image storage, or technical services necessary to provide our platform.

These service providers may process information on our behalf and are expected to handle it in accordance with applicable privacy and security requirements.

We may also disclose information where required by law, where necessary to protect our rights or the security of our platform, or in connection with a business transfer, merger, or restructuring, subject to applicable privacy laws.

### 6. Storage and Security

We take reasonable measures to protect the personal information we collect against unauthorized access, loss, misuse, alteration, or disclosure.

Your account information, saved activities and uploaded project photos may be stored and processed through third-party technology providers that support our website and its features. Depending on the services used, your information may be stored or processed in Canada or other jurisdictions.

All photo files are held in storage with access controls. Private photos are available only to their owner. Photos explicitly shared publicly are served through the public activity gallery until you make them private or remove them, or they are hidden after a report. We process uploaded images to create suitable display versions and remove embedded metadata, such as location information. Removing metadata does not remove identifying details visible within an image, so please check the photo before uploading it.

While we take reasonable steps to safeguard your information, no method of electronic storage or transmission over the internet is completely secure, and we cannot guarantee absolute security.

### 7. Data Retention

We retain personal information only for as long as reasonably necessary to provide our services, maintain your account, fulfill the purposes outlined in this Privacy Policy, or meet applicable legal obligations.

You can remove a saved project or delete an uploaded photo through your account. Removing a saved project also removes the progress and private photos attached to that saved project. It does not remove the general activity from our catalogue. Gallery uploads are separate from saved projects: manage them under Your gallery shelf in My projects. Make private removes public access while keeping your copy; Delete permanently removes that gallery photo. Deleting your account removes both private and shared photos. A reported gallery photo is hidden from public view and cannot be republished using the owner controls; the owner can delete it. Reports record the reporting account, photo, selected reason and time, and are removed when the reported photo or the reporting account is deleted.

If you delete your account or request the deletion of your personal information, we will take reasonable steps to delete your information, subject to legal requirements and any limited information that may need to be retained for legitimate purposes. Limited copies may remain in protected backups until those backups expire under the applicable retention schedule; they are not available through your account.

Guest progress remains on your device until you delete it or your browser clears it. Clearing browser data does not delete a signed-in account's server-stored information. Copies you download, export or print are under your control and are not removed when you delete your account.

### 8. Your Privacy Rights and Choices

You have the right to request access to the personal information we hold about you and to request corrections if that information is inaccurate or incomplete.

You may also request that we delete your account and associated personal information, subject to applicable legal requirements.

Account settings allow you to edit optional profile information and request account deletion. My projects lets you remove saved projects, manage favourites, delete or download private project photos, and manage photos you have shared publicly. Progress backup exports contain saved progress and do not include photo files. We may need to verify your identity before completing an account or privacy request.

If you wish to access, correct, or delete your information, or if you have questions about how we handle your personal information, you can contact us using the contact information provided below.

### 9. Cookies and Website Technologies

Our website uses essential cookies or similar technologies to support website functionality, maintain account sessions, and provide a reliable user experience. Browser storage supports guest activity progress and preferences. These functions do not automatically synchronize guest data with an account.

We do not use advertising trackers in this release. If additional technologies are introduced to understand website usage or improve our platform, this Privacy Policy will be updated to reflect those practices, with any required choices presented before use.

You may be able to manage cookies through your browser settings. Disabling certain cookies may affect the functionality of the website or your ability to sign in. Clearing browser storage may remove locally saved guest progress.

### Feedback and ideas

When you send feedback, we send your message, chosen category, current page or activity, and optional reply email to naturesmossyfriends@icloud.com through FormSubmit. We do not attach your account details or photos. Short-lived hashed request identifiers help limit spam. Please do not include children’s personal information. FormSubmit processes the submission to deliver the email; our team retains received feedback in its inbox. You can request deletion through our privacy contact.

### 10. Third-Party Links and Services

Our website may contain links to external websites, platforms, or resources that are not operated by Natures Mossy Friends.

We are not responsible for the privacy practices, content, or security of third-party websites. We encourage you to review their privacy policies before providing personal information to them.

### 11. Changes to This Privacy Policy

We may update this Privacy Policy from time to time to reflect changes to our website, features, services, or applicable privacy laws.

Any updates will be posted on this page with an updated revision date and, where applicable, a revised effective date. We encourage you to review this Privacy Policy periodically. If a change requires a new acknowledgement or other choice, we will present it before the affected feature is used.

### 12. Contact Us

If you have questions, concerns, or requests regarding this Privacy Policy or your personal information, please contact us:

**Natures Mossy Friends**  
**Email:** naturesmossyfriends@gmail.com

We are committed to responding to privacy-related inquiries and addressing concerns in a reasonable and timely manner.

Thank you for being part of Natures Mossy Friends and helping us create more opportunities for creativity, curiosity, and meaningful moments together.
