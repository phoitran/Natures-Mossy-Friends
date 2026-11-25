# API and data model

This is the app's internal same-origin API, not a separately versioned public developer service. Route files are authoritative. JSON responses generally use `{ "error": "..." }` on failure. Mutations require an `Origin` matching the request URL. A missing origin is rejected, so a command-line test needs an explicit local origin.

## Routes

| Route | Methods and operation | Access |
| --- | --- | --- |
| `/api/account` | GET session/profile/configuration readiness; POST adult/policy acknowledgement and optional name; DELETE account and associated app data | Readiness can be read without an account; mutations require identity |
| `/api/auth` | POST `signup`, `signin`, `reset`, `resend`, `signout` | Independent Firebase build only; normal Sites mode returns 404 |
| `/api/projects` | GET projects, favourites, private-photo metadata; POST favourite toggle or project revision; DELETE `?id=` | Registered adult account, restricted to owner |
| `/api/photos` | POST JPEG bytes with `?project=`; GET `?id=` and optional `download=1`; DELETE `?id=` | Private owner access |
| `/api/creations` | GET `?activity=` with optional cursor; GET `?id=` image; GET `?mine=1`; POST JPEG with `?activity=`; PATCH visibility/report; DELETE `?id=` | Public reads only for public creations; adult account for uploads/actions and private shelf |
| `/api/feedback` | POST validation, honeypot and throttle; returns `{ok, deliver}` | No account needed; same-origin required; actual delivery is a later browser request to FormSubmit |

Gallery upload additionally requires `x-share-confirmed: yes`. Re-sharing requires PATCH `{id, action: "public", confirmed: true}`. Withdrawal uses `action: "private"`; reporting uses `action: "report"` and a reason of `privacy`, `inappropriate` or `not-a-project`. A hidden creation cannot be re-shared by its owner.

Example project body (values are artificial):

```json
{
  "id": "90af7dd4-66a9-45d2-8bfe-dd45628af1db",
  "activityId": "SUM-06",
  "variant": "little",
  "step": 1,
  "status": "in-progress",
  "revision": 1
}
```

The server returns the new revision. Send the latest revision on the next update; HTTP 409 means reload and reconcile. Valid variants are `little`, `young` and legacy `together`, subject to each activity's eligibility. Valid project statuses are `in-progress` and `completed`; step values range from 0 to 5. Favourites use `{kind: "favourite", activityId, saved: true/false}` instead.

## Data tables

| Table | Main contents and links |
| --- | --- |
| `accounts` | Identity ID, adult email, optional name, policy version, creation time, photo-byte accounting |
| `projects` | ID, owner ID, activity ID, age variant, current step, status, timestamp and revision |
| `favourites` | Owner/activity associations |
| `photos` | Private photo ID, owner and project IDs, R2 object key, bytes, MIME and timestamp |
| `creations` | Separate gallery photo ID, owner/activity IDs, object key, byte size, `public`/`private`/`hidden` state and timestamp |
| `creation_reports` | Creation ID, reporter ID, predefined reason and timestamp; unique reporter/creation pair |
| `auth_attempts` | Hashed throttle identifiers, attempt counts and expiry; also used by feedback throttling |

These are logical associations; do not assume every relationship is enforced by a database foreign key. Handlers enforce ownership and cleanup. Public gallery responses exclude email, owner ID and storage keys; they expose display identifiers, activity, timestamp, state and a viewer-specific `mine` flag.

## Limits and failure handling

- Up to 50 projects per adult account.
- Three private photos per project; six gallery creations per activity per account, 60 gallery creations total per account.
- Shared photo storage budget: 157,286,400 bytes (150 MiB) per account.
- Client input: JPG/PNG/WebP up to 10 MiB and 25 megapixels, re-encoded to JPEG. HEIC needs conversion first.
- Feedback: message up to 2,000 characters, optional reply email up to 254; app endpoint permits three requests per 15-minute fingerprint window. External provider controls are separate.
- Auth: same-origin checks, bounded inputs and action/email/IP-derived throttles in standalone mode. No raw passwords are stored in D1.
- Typical statuses: 400 invalid input, 401 missing identity, 403 wrong origin, 404 missing/not-owned item, 409 revision or visibility conflict, 423 registration unavailable, 429 throttled, 500/503 storage/provider failure.

Object storage and database operations are not one distributed transaction. The code includes quota reservation and failure cleanup, but operators still need reconciliation, backup and recovery procedures. Account deletion removes application data and then independent Firebase identity; a provider failure can leave identity deletion retryable. Backups/retention require operator policy beyond these handlers.
