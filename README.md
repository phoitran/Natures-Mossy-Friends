# Natures-Mossy-Friends

**University of Calgary - Haskayne School of Business**

**ENTI 333 L02 Group 17:** Khadija Adeeb, Harli Cameron, Ren Chen, Diana Garcia Martinez, Nabiha Khan, and Phoi Tran

Little things. Big imaginations. Made for the moments together.

A website for teachers and parents with children aged 4-12 to find easy and fun arts and craft activities made entirely with organic and eco-friendly materials.

[Visit the website](https://natures-mossy-friends.natalieforstbauer.chatgpt.site/) · [Features](docs/FEATURES.md) · [Setup](docs/SETUP.md) · [Technical architecture](docs/ARCHITECTURE.md) · [AI assistance](docs/AI_ASSISTANCE.md)

## What is the app?
The app is a centralized website consisting of a variety of arts and crafts activities that can be done entirely by eco-friendly and natural materials that are easily found in nature. Guardians and children alike can browse through different examples of activities that are separated by seasons or age group. Selecting one of these activity would give users examples of end results, a list of necessary materials and five illustrated steps allowing for user to follow along easily. 

Users can also save an idea, resume unfinished crafts, or share a picture of their personal creation in the activitiy's gallery. The goal of the app to provide guardians and children fun and creative crafts that reduce waste and encourage outdoor activities.

## Features

**Find your next activity:** With over fifteen crafting ideas, users can filter by age group, seasonality, time required, or materials.

**Surprise me:** After selecting the season and age range, the user can be recommended an activity without the stress of choosing.

**Save your favorites:** Each activity contains a discription and picture for easy selection. User can choose to save an activity which can be found under 'My projects'.

**One step at a time:** Each activity contains five steps with personalized illustrations and easy to understand instructions.

**Read-aloud:** some activities have the option to narrate the instruction at each step.

**Track your progress:** Under 'My projects', users can also view previously worked on projects or activities currently being done. Creating an account would allow this to be accessible across devices.

**Photo guide:** a short photo guide that illustrates and explain the steps with caption and music.

**Print guide:** Guardians can print the list of materials, steps of the activities and images of possible creations.

**Share your wonder:** user has the choice to share an image of their completed project and view others from the community.

**Join the fun:** Users can make an account with their ChatGPT account to gain access to projects across all devices (in development)

## Run locally

Use **Node.js 24**, npm, and the checked-in lockfile. No cloud account is needed for guest browsing or isolated tests.

```sh
npm run install:ci
npm run dev
```

Open the localhost address printed by the server (normally `http://localhost:5173`). Local account/gallery testing also needs an ignored `.dev.vars` file and local database migrations: follow [SETUP.md](docs/SETUP.md). The portable development server supplies a clearly synthetic local sign-in identity; it is not production authentication.

```sh
npm test
npm run typecheck
npm run build
```

Media checks additionally need Python 3, Pillow and FFmpeg/ffprobe:

```sh
python3 -m pip install -r requirements-dev.txt
npm run test:media
```

[Latest export verification](docs/EXPORT_VERIFICATION.md) records what was actually run and any limitations. [Testing guide](docs/TESTING.md) explains each suite.

## Technical components

| Component | Role |
| --- | --- |
| React 19 + TypeScript | Interactive interface, state, forms and reusable components |
| Vinext + Vite | Next-compatible application routing and server/client builds |
| Tailwind CSS 4 + custom CSS | Styling, responsive layouts, print styles and motion preferences |
| Cloudflare Workers | Server-side application and API execution |
| Cloudflare D1 + Drizzle | SQLite-backed accounts, projects, favourites, photo metadata, reports and throttling records |
| Private Cloudflare R2 bucket | Uploaded photo bytes, served through access-controlled routes |
| ChatGPT Sites identity | Current production identity provider |
| Firebase Authentication REST API | Prepared independent email/password mode; not a running second deployment |
| FormSubmit | Browser-to-provider feedback email submission after app-side validation |
| MP4 / WebVTT / WebP / SVG / MP3 | Pre-generated tutorials, captions, images, diagrams and read-aloud recordings |

See [architecture](docs/ARCHITECTURE.md), [API and data model](docs/API.md), [security](SECURITY.md) and [deployment](docs/DEPLOYMENT.md). Exact package versions are in `package-lock.json`.

## Repository guide

```text
app/                   Pages, interactive UI and API routes
components/, hooks/    Reusable interface utilities
lib/                   Authentication, storage, discovery, upload and audio helpers
content/               Activity, privacy, video, caption and narration JSON
public/assets/         Browser-ready images, diagrams, videos, music and narration
assets/source/         Editable original generated image files
worker/                Sites and independent Worker entrypoints
db/, drizzle/          Schema and ordered SQL migrations
deploy/                Placeholder configuration for independent hosting
scripts/               Development, build, deployment and media-production tools
tests/                 Content, route, auth, feedback, discovery, narration and media checks
docs/                  Product, architecture, setup, testing and provenance documentation
.github/workflows/     Automated checks for pushes and pull requests
LICENSE                Existing MIT software license, retained unchanged
THIRD_PARTY_NOTICES.md  Dependency, media and narration licensing boundaries
```

This export includes all tracked application files and shipped media from the source snapshot, plus updated documentation and developer check scripts. It excludes dependencies, compiled output, Git history, credentials, production databases and user-uploaded photos. Install dependencies instead of committing `node_modules`.

## Documentation and coursework evidence

| Requirement | Evidence in this repository |
| --- | --- |
| Explain what the app is and who it serves | This README; [FEATURES.md](docs/FEATURES.md); [PRD.md](docs/PRD.md) |
| Explain its features and limitations | [FEATURES.md](docs/FEATURES.md); [ROADMAP.md](docs/ROADMAP.md) |
| Explain technical components | [ARCHITECTURE.md](docs/ARCHITECTURE.md); [API.md](docs/API.md) |
| Provide setup and verification instructions | [SETUP.md](docs/SETUP.md); [TESTING.md](docs/TESTING.md) |
| Include a license file | [LICENSE](LICENSE); [third-party notices](THIRD_PARTY_NOTICES.md) |
| Disclose AI assistance | [AI_ASSISTANCE.md](docs/AI_ASSISTANCE.md); original prompt/production notes in `docs/` |
| Make the work reviewable on GitHub | [GITHUB_SETUP.md](docs/GITHUB_SETUP.md); upload the extracted source and give the instructor repository access |

Documentation and code are ready for repository review. This file does not claim the GitHub upload is complete, a grade is guaranteed, or a Replit deployment exists.

## AI assistance and authorship

Harli supplied the product idea, activity references, requirements and iterative feedback. ChatGPT/Codex assisted with implementation, debugging, documentation and test execution. AI image generation produced inspiration imagery, and ElevenLabs generated the selected recorded narration. See [AI_ASSISTANCE.md](docs/AI_ASSISTANCE.md) for scope, evidence and limitations. No prompt history containing private information or credentials is included.

## License

The existing [MIT License](LICENSE) is retained, including its original copyright notice. Vendored libraries retain their own notices. The software license is not a blanket grant of rights to third-party media, voices, trademarks or user submissions. The Shelley audio was produced under a noncommercial service plan; review [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) before redistribution or commercial deployment.

## Contributing

Start with [CONTRIBUTING.md](CONTRIBUTING.md). Do not change existing activity IDs or rewrite applied migrations. Keep the live site, content manifests, media and documentation consistent, and use artificial data for tests.
