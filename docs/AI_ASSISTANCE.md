# AI assistance and project authorship

## Disclosure

Natures Mossy Friends was developed with AI assistance. This document distinguishes the owner's decisions from generated implementation and media. It is not a claim that every file was manually written or that automated checks establish real-world craft safety.

| Contributor or tool | Contribution | Evidence and boundaries |
| --- | --- | --- |
| Harli Cameron, product owner/student | Product idea, audience, activity choices, reference images, requested wording, colour/motion preferences and iterative feedback | Owner requirements reflected in the PRD and current catalogue; no fabricated interviews or testing claims |
| ChatGPT / Codex | Help with requirements, React/TypeScript implementation, API/storage logic, debugging, tests, technical documentation and export preparation | Source, tests, documentation and recorded QA history; generated code requires review and maintenance |
| AI image generation | Original inspiration galleries and realistic photo-step panels informed by supplied references | Prompt/production notes in `docs/`; editable originals in `assets/source/`; these are not participant photos |
| Code-based illustration and video tooling | SVG diagrams, image composition, captioned photo videos and locally composed instrumental music | Generation scripts and media manifests in this repository; deterministic output still needs visual review |
| ElevenLabs | Shelley read-aloud audio for SUM-06, including age variants | `content/narration.json` and `docs/narration.md`; no voice-generation API key shipped |

## Examples of owner-led iteration

- Added summer mandalas, rocky friends, wilderness creatures and sand mazes, then winter snow people, villages and animals.
- Revised winter imagery to include distinct reference-inspired variations; changed snow-mouse ears and leaf-owl eyes to pebbles.
- Replaced longer tutorials with 60–90-second realistic photo steps; the current active videos are 75 seconds.
- Removed the dedicated Make Together section, kept legacy saved mixed-age projects, and added filtered Surprise me.
- Added separate public completed-project galleries while retaining private projects and photos.
- Added an on-page feedback form; adjusted pastel colours, butterflies and four-second cover transitions.
- Requested independent email signup and selected a specific narration voice, with gradual rollout.

These summarize requirements, not a verbatim transcript. No private chat history, credentials, reference-upload screenshots or customer data is needed to review the code.

## How output is checked

Content checks validate identifiers, age eligibility and referenced assets. Isolated route/auth tests exercise real handlers with substituted database, bucket and identity-provider dependencies. Media tests inspect shipped files, captions, chapters and revision hashes. Type checking and builds catch integration errors. Historical visual-review notes live in `docs/QA.md`; this export's actual commands and results live in `docs/EXPORT_VERIFICATION.md`.

Generated instructions and example imagery still need hands-on adult trials. Mocked authentication and email tests do not prove real provider delivery or successful signup. No usability study, market demand, revenue or accessibility certification is claimed.

## Runtime use of AI

Visitors do not trigger image, text or narration generation. The site serves prepared assets and may use the browser's speech-synthesis feature. Uploaded project photos are not sent to generative AI. Adding any future runtime AI feature requires its own privacy, cost and behaviour review.

## Academic use

The student should review this code and documentation, understand the main components and explain the choices during assessment. Follow the course's actual AI-disclosure and repository-access requirements. This disclosure supplies evidence of AI assistance; it does not substitute for instructor approval or a required personal reflection.
