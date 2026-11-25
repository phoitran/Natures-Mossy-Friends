# Local development

## Requirements

- Node.js 24 and npm. `package.json` permits Node >=22.13.0, but the export checks use Node 24; the route suites use Node's built-in SQLite module.
- A current browser. Guest mode needs no Firebase or Cloudflare account.
- Python 3, Pillow and `ffprobe` for media verification; FFmpeg for video regeneration.
- Enough disk space for approximately 253 MB of authored source/media plus installed packages and build output.

The lockfile is committed. Use it; do not replace package versions merely to make an install warning disappear.

## Install and browse

From the extracted project folder:

```sh
npm run install:ci
npm run dev
```

Open the server's localhost URL. Stop it with Ctrl+C. If the port is occupied, use the alternative URL printed by the server or stop the conflicting process.

Guest favourites and progress use this browser's local storage. They do not automatically transfer to another port, domain, browser or device.

## Local accounts, database and photo testing

1. Copy `.dev.vars.example` to `.dev.vars`. Leave Firebase values blank for the ordinary Sites-mode local preview.
2. Keep `PRIVACY_CONTACT_EMAIL` set to a nonempty development contact. The example uses a non-deliverable address so it cannot be mistaken for a working inbox.
3. Build to generate the local Wrangler configuration:

   ```sh
   npm run build
   ```

4. Apply the three existing SQL migrations to **local** storage. Run these separately, in order; omit neither `--local` nor `--persist-to`:

   ```sh
   npx wrangler d1 execute DB --local --persist-to .wrangler/state --config dist/server/wrangler.json --file drizzle/0000_curvy_albert_cleary.sql
   npx wrangler d1 execute DB --local --persist-to .wrangler/state --config dist/server/wrangler.json --file drizzle/0001_clear_captain_marvel.sql
   npx wrangler d1 execute DB --local --persist-to .wrangler/state --config dist/server/wrangler.json --file drizzle/0002_aromatic_young_avengers.sql
   ```

5. Run `npm run dev` again. Portable local development has a synthetic sign-in identity (`seedy@sites.test`) restricted by the development plugin to loopback hosts. It exists only to exercise local workflows. No real ChatGPT account is being created or authenticated.

Run those SQL files once per fresh local database. If tables already exist, do not blindly rerun or delete data: inspect the local state first. Never use `--remote` for this local setup. Local data in `.wrangler/` must not be committed.

The app needs both `DB` and `BUCKET` bindings for account and photo features. Guest browsing can work while account services are unavailable. Isolated tests create their own in-memory databases and do not need these manual local migrations.

## Environment and configuration

| Name or file | Purpose | Handling |
| --- | --- | --- |
| `PRIVACY_CONTACT_EMAIL` | Enables account registration and supplies the operational privacy contact | Local `.dev.vars`; deployed runtime configuration |
| `FIREBASE_PROJECT_ID` | Independent authentication project | Required only for standalone mode |
| `FIREBASE_API_KEY` | Server-side Firebase REST project key | Ignored local variables or deployment secret input; never put a real value in examples |
| `.openai/hosting.json` | Original Sites project identity and storage binding names | Included for source fidelity; project ID is not a credential or permission to deploy |
| `wrangler.standalone.json` | Owner-specific independent Worker/resource configuration | Ignored; create from `deploy/wrangler.example.json` only when configuring a new deployment |
| `__MOSSY_STANDALONE__` | Build-time identity-mode switch | Set by `vite.standalone.config.ts`, not a runtime user input |

Feedback's destination is currently in `lib/feedback-delivery.ts`; it is not controlled by `PRIVACY_CONTACT_EMAIL`. Its email delivery is a separate operational dependency. Do not send test mail to the owner's real inbox without agreeing a test first.

## Build modes

- `npm run build`: the source's Sites-compatible server/client build.
- `npm run start`: serves built output with Wrangler locally; this is not a production deployment or the development mock-sign-in middleware.
- `npm run build:standalone`: builds the independent Firebase-auth Worker. With blank example settings it is a build check, not a configured live signup service.
- `npm run dev:standalone`: local independent-mode development after its own configuration.
- `npm run deploy:standalone`: **changes a real Cloudflare deployment** when credentials and configuration are present. Read [DEPLOYMENT.md](DEPLOYMENT.md) before using it.

## Checks and troubleshooting

```sh
npm test
npm run typecheck
python3 -m pip install -r requirements-dev.txt
npm run test:media
```

If installation fails, keep the lockfile and examine the error, network access and Node version. If a native package install script was blocked, review the named package and npm policy; do not approve every script blindly. If `ffprobe` is missing, install FFmpeg for the operating system. If a gallery gives a service-unavailable message locally, check migrations and bindings; do not treat it as evidence that a live gallery is broken.

Hosting, email, actual phone uploads and browser acceptance require separate checks. [TESTING.md](TESTING.md) distinguishes them from isolated tests.
