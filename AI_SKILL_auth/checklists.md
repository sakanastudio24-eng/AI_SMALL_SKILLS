# Auth Checklists

## Flow Design

- Identify app type: SSR web, SPA, mobile, public API, admin tool.
- Identify identity source: first-party, external IdP, hybrid.
- Identify sensitive actions that need step-up auth or MFA.
- Decide the session/token lifetime and refresh behavior.
- Decide how logout and revocation behave across devices.

## Security Review

- Use httpOnly cookies when browser auth can be same-origin.
- Use PKCE for public OAuth clients.
- Validate redirects against an allowlist.
- Add CSRF protection for cookie-backed browser auth.
- Hash passwords with a modern password hasher if passwords exist.
- Rate-limit login, reset, and verification endpoints.
- Log security-sensitive admin and account actions.
- Validate provider and webhook signatures.

## Authorization

- Define roles and capabilities separately.
- Check both route-level and resource-level access.
- Prevent users from acting on resources they do not own.
- Keep admin powers explicit, narrow, and auditable.
