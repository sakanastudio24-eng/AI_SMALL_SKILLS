# OAuth Flow Template

## Provider

- provider name:
- scopes:
- public or confidential client:

## Required Flow

1. User starts auth at provider.
2. App sends state, nonce if needed, and PKCE challenge for public clients.
3. Provider returns authorization code.
4. Backend exchanges code for tokens.
5. App validates issuer, audience, expiry, and nonce/state.
6. App maps external identity to local user/account.
7. App creates local session and redirects safely.

## Decisions

- account linking policy:
- new-user onboarding policy:
- session lifetime:
- refresh token handling:
- revocation behavior:

## Security Rules

- use PKCE:
- allowed redirect URIs:
- token storage:
- provider claims required:
- error handling path:
