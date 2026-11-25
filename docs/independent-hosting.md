# Independent signup and hosting

Prepared 22 November 2026. This is a separate deployment; the existing ChatGPT Site remains live with its existing authentication and data. The independent version has not been deployed or connected to a real Firebase project. No Cloudflare resources or paid subscriptions have been created.

## Accounts the owner needs

1. Create a Cloudflare account at <https://dash.cloudflare.com/sign-up>. Verify the email. There is no need to buy or transfer a domain. Workers provides an address of the form `https://natures-mossy-friends.<account-subdomain>.workers.dev`, subject to availability. Start on Workers Free.
2. Open <https://console.firebase.google.com/> using a Google account. Create a project named Natures Mossy Friends on the Spark plan. Analytics is optional and is not used by this app. Do not enable App Hosting, phone authentication, or Firebase Storage for this deployment; those are not needed here.
3. In Firebase Authentication, enable Email/Password (not email-link login). Set the password policy to at least 12 characters and enable email-enumeration protection. Add the eventual Workers hostname to the authorized domains. Register a Web app to obtain the Firebase project ID and Web API key. Configure verification and reset templates with the app name. Firebase's hosted email-action pages are used for verification and resets.

Ordinary users can then create accounts with their own email address and password. They do not need Google, Cloudflare, or ChatGPT accounts. Google and Cloudflare accounts are only for the site owner.

## Free usage and billing

- Cloudflare Workers Free currently includes 100,000 dynamic requests/day and a 10 ms CPU limit per request. A free `workers.dev` address avoids domain registration costs. Performance and CPU use still need measurement on the deployed app.
- D1 offers a free allocation for account records. Check current quotas before launching.
- R2 Standard includes 10 GB-month storage, 1 million Class A operations and 10 million Class B operations/month. It requires a subscription checkout and billing setup; usage beyond the allowance is billable. Do not describe this as guaranteed free forever or enable it without the owner's billing decision. Per-account upload quotas already exist, but they do not cap total storage across all users.
- Firebase Spark needs no payment method. Email/password authentication is available on the free plan. Current daily mail limits include 1,000 verification messages and 150 password resets. Email-link sign-in has a much smaller free limit, so this implementation uses passwords. No custom sender domain or SMTP subscription is required for the default Firebase templates.
- This replaces the earlier Supabase email-code proposal. Supabase's default SMTP only sends to project-team addresses and cannot serve public signup without additional email-delivery setup.

Pricing sources: <https://www.cloudflare.com/plans/developer-platform/>, <https://developers.cloudflare.com/workers/configuration/routing/workers-dev/>, <https://developers.cloudflare.com/d1/platform/pricing/>, <https://developers.cloudflare.com/r2/pricing/>, <https://developers.cloudflare.com/r2/get-started/>, <https://firebase.google.com/pricing>, <https://firebase.google.com/docs/auth/limits>.

## Deployment preparation

The normal `npm run build` remains the Sites build. `npm run build:standalone` uses `vite.standalone.config.ts` and a plain Worker entrypoint, omits Sites integration, and fixes the auth mode at build time. Missing Firebase configuration disables signup; it never falls back to trusting platform identity headers.

Create a D1 database and, after the owner accepts the billing terms, a private R2 Standard bucket. Do not enable public R2 access. Copy `deploy/wrangler.example.json` into the project root as `wrangler.standalone.json` (ignored by Git), then adjust:

- `$schema` to `./node_modules/wrangler/config-schema.json`;
- `main` to `./worker/standalone.ts`;
- `d1_databases[0].migrations_dir` to `./drizzle`;
- the D1 database ID, database name, R2 bucket name, Worker name and Firebase project ID;
- keep the real privacy contact and `workers_dev: true`.

Run Wrangler login locally or use an approved connected account. Store the Firebase API key through Wrangler's secret input as `FIREBASE_API_KEY`, not in source, chat, command arguments or a committed config. For local development use an ignored `.dev.vars` file. No Firebase service-account private key is needed. The Web API key identifies the project; restrict it to the Firebase Authentication APIs rather than applying browser-referrer restrictions to these server-side calls.

Apply the SQL migrations to the new D1 database using `wrangler d1 migrations apply DB --remote --config wrangler.standalone.json`. These migrations create tables; they do not copy old site data. Set the Worker secret, then run `npm run deploy:standalone` from an authenticated Cloudflare environment. The script checks the config, runs type and auth checks, builds the independent bundle and deploys that bundle only. If the initial secret setup needs an existing Worker, deploy with signup disabled first, set the secret, and re-test before announcing signup.

Before opening registration, test a new adult account, real verification delivery, sign-in, password reset, sign-out, private-photo loading, explicit public sharing, cross-account isolation, and account deletion on the new host. Account deletion requires a login within the last four minutes. The current implementation deletes the user's app data first and then Firebase identity; on an upstream failure, the user remains able to sign in and retry cleanup. Firebase verification/reset email delivery and real Cloudflare execution cannot be verified until these accounts exist.

## Existing projects and photos

Do not remove the original site or database during cutover. Firebase identities use a separate namespace and are never linked to an old account merely because someone submits the same email.

The existing owner-controlled export/import supports project progress and favourites. An owner can sign in to the old site, export a progress backup, create and verify an independent account, and import the backup there. Photo files must be downloaded from their projects and uploaded again; public sharing must be explicitly selected again. Guest progress is origin-specific, so it also needs export/import when moving to a new web address.

For a future bulk migration, obtain consistent database and object backups, securely verify the old-to-new account mapping, rewrite every ownership reference together, validate counts/object checksums, and test rollback before switching addresses. This has not been performed. No old credentials can or should be copied into Firebase.

## Security and validation

Firebase's documented REST API handles signup, sign-in, verification mail, password recovery, token refresh, account lookup and identity deletion. Tokens stay in Secure, HttpOnly, host-only SameSite cookies. Every authenticated data request is checked with Firebase, then constrained to the configured project and account owner. Unverified accounts cannot save or access private data. Auth mutations require same-origin requests, bounded input and D1 throttling; passwords and raw email/IP values are not stored in the throttle table.

`node tests/auth.test.mjs` verifies the independent server behavior against a simulated provider, including spoofed-header rejection, missing-config behavior, verification gating, project scope, token refresh, mail errors, throttling, private-image access, ownership and deletion. `node tests/routes.test.mjs` verifies the existing Sites behavior. These tests do not prove real provider configuration or email delivery.

Auth reference: <https://firebase.google.com/docs/reference/rest/auth>.
