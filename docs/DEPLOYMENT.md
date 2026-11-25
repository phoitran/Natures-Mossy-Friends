# Deployment and hosting boundaries

## Current publication

The exported application corresponds to ChatGPT Sites version 21 at:
https://natures-mossy-friends.natalieforstbauer.chatgpt.site/

Original source commit: `68ddd584154fa7324ea6554da003131b37a6cf59`.

This GitHub preparation does not redeploy or change that site. `.openai/hosting.json` retains the original project identifier for provenance and build compatibility; it is not a credential. Only an authorized project editor can publish to that project through Sites.

## GitHub is the source repository

Store source, documentation, migrations, tests and media in GitHub. Do not upload only the ZIP, dependencies, compiled output or production data. Repository publication does not automatically migrate the running site or user accounts.

This application's Workers APIs and D1/R2 dependencies cannot run on GitHub Pages as-is. A Pages link is not a replacement deployment. Ordinary shared hosting also needs a verified server/runtime plan; copying the folder into a public web directory is insufficient.

## Prepared independent mode

The code includes `vite.standalone.config.ts`, `worker/standalone.ts`, Firebase auth handlers, a placeholder Wrangler configuration and a deployment helper. This mode was prepared to remove the visitor's ChatGPT-account requirement. It still uses Workers, D1 and R2; it is not a generic PHP or Node-hosting port.

Read [independent-hosting.md](independent-hosting.md) for configuration steps. That file records the earlier preparation date and provider terms at that time; recheck quotas, pricing and licensing before provisioning resources. Real account configuration, email delivery and deployment are still outstanding.

The independent sequence is: provision approved resources, create private bucket/database, configure Firebase, apply migrations, add secrets outside source control, build, deploy, run real-provider acceptance, then consider changing the public URL. Never deploy the Sites identity mode on an untrusted server or enable public R2 access for private photos.

## Replit and ExclusiveHosting

The PRD discusses Replit as a possible course target; no Replit build has been deployed. Moving requires a proven frontend/server build, adapted database/storage calls and independent account integration. Replit Auth and Clerk Auth are distinct options, as documented in the PRD.

ExclusiveHosting has been discussed as a possible destination. Its actual account capabilities, Worker alternatives, Node support, storage and deployment workflow have not been verified here. This package preserves the source for that investigation; it does not claim compatibility with a hosting plan that has not been inspected.

## Data migration and recovery

Keep the existing site available during migration. New provider accounts must not be linked solely by a matching email submitted by a visitor. Guest storage is origin-specific. Supported manual transfer currently consists of project/favourite JSON export/import and separate photo download/re-upload; sharing requires fresh consent.

Any bulk move needs verified backups, explicit account mapping, record/object counts, checksums and a tested rollback. No live database, uploaded photo, session or credential is included in this source export.
