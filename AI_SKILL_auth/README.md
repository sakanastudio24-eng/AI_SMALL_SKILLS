# AI_SKILL_auth

## Purpose
Handle authentication and authorization flows safely and correctly.

## Use When
- implementing login
- handling OAuth
- magic link flows
- session persistence
- designing protected routes
- reviewing auth security boundaries

## Do Not Use When
- building unrelated API routes
- doing frontend-only styling work
- reviewing non-auth business logic

## Steps
1. Identify auth type and trust model.
2. Choose the safest practical session or token model.
3. Configure the provider or auth backend.
4. Handle callback, session creation, and redirect rules.
5. Validate authorization, expiry, recovery, and logout behavior.

## Constraints
- never expose service role keys
- verify redirect URLs
- handle expired and revoked sessions
- keep authorization checks on the server

## Related Skills
- AI_SKILL_web
- AI_SKILL_system_design
