# Magic Link Flow Template

## Goal

Describe the product goal for magic link login and the user type it serves.

## Entry Points

- sign-in page:
- invitation acceptance:
- checkout or gated action:

## Flow

1. User submits email.
2. System validates rate limit and account status.
3. System creates a short-lived, single-use token.
4. System sends a signed link to the email address.
5. Callback verifies token, expiry, audience, and redirect target.
6. Session is established.
7. User is redirected to the correct post-login destination.

## Security Rules

- token lifetime:
- single-use enforcement:
- redirect allowlist:
- rate limit:
- session duration:
- post-login device/session metadata to store:

## Failure States

- expired link:
- reused link:
- unknown email:
- invite no longer valid:
- blocked account:
