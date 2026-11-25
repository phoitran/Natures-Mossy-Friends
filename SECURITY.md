# Security and privacy notes

## Report a vulnerability

Do not post credentials, personal data or exploit details in a public issue. The application's published privacy contact is `naturesmossyfriends@gmail.com`; delivery and monitoring must be confirmed by the owner. If it is unavailable, contact the repository owner privately through an already established channel. No response-time guarantee or bug-bounty programme is established.

## Implemented controls

- Adult account and policy acknowledgement before owned account features.
- Same-origin mutation checks, bounded JSON input, prepared SQL queries and owner-constrained access.
- Revision conflicts for project edits; photo and project quotas.
- Private R2 storage and route-mediated photo delivery; explicit sharing and report-triggered hiding.
- JPEG re-encoding and metadata checks for uploads; no public owner email or storage keys.
- Independent authentication isolated at build time, with verified identity and secure session cookies.
- Ignored local configuration; no credentials or production user data in the export.

## Limits requiring an operator

This is a prototype, not a security certification. Automated route tests substitute providers and storage. Public uploads do not have automatic image-content screening or a moderator dashboard. Reports can be abused; a human resolution process remains necessary. Feedback's external provider can be called without passing through the app's own throttle. Provider activation, monitoring, retention, backup recovery, dependency advisories and real cross-account acceptance need operational attention.

Do not expose development mock identity or the Sites header-based identity mode on an arbitrary public host. Do not enable public access to the upload bucket. Do not use real child data in testing. If a secret is committed, revoke/rotate it with its provider; deleting the current file does not remove it from Git history.
