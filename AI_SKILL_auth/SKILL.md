---
name: AI_SKILL_auth
description: Design, review, and implement authentication and authorization flows for web and API systems. Use when users ask about sign-in, sessions, OAuth, RBAC, protected routes, token handling, account security, or auth architecture decisions.
---

# AI_SKILL_auth

## Overview

Use this skill for auth work spanning login flows, session models, access control, and security-sensitive integration choices. Default to the safest practical model for the actual product shape.

## Execute Workflow

1. Identify the auth surface.
- Determine app type, client types, identity providers, and protected resources.
- Separate authentication from authorization requirements.
- Identify whether the product is:
  - server-rendered web app
  - SPA with backend API
  - native/mobile client
  - third-party/public API
  - internal admin surface

2. Gather the trust model.
- Identify user types, admin roles, external integrations, and session lifetime expectations.
- Note whether the system handles sensitive business data, payments, health data, or destructive admin actions.
- Clarify whether auth is first-party, delegated to an identity provider, or hybrid.

3. Choose the auth model.
- Prefer these defaults unless constraints say otherwise:
  - server-rendered web app: httpOnly session cookies
  - same-origin SPA + backend: cookie/session model if possible
  - public OAuth clients: Authorization Code with PKCE
  - machine-to-machine: scoped service credentials
  - third-party API consumers: short-lived bearer tokens with clear revocation model
- Avoid long-lived tokens in browser storage when cookies can solve the problem more safely.

4. Define authorization clearly.
- Map roles, permissions, and resource ownership rules.
- Avoid vague “admin” behavior without explicit capability boundaries.
- Prefer capability-based rules over broad role names alone.
- Check both route-level and resource-level authorization.

5. Check security controls.
- Review password handling, token storage, session expiration, CSRF, redirect validation, and secret management.
- Identify account recovery, logout, and revocation requirements.
- Also verify:
  - MFA or step-up auth for sensitive actions
  - email verification or account proofing needs
  - rate limits and lockout behavior
  - audit logging for admin/security actions
  - webhook signature validation when external auth providers are involved

6. Produce implementation guidance.
- Specify route protection, backend checks, and client-state behavior.
- Include failure states and edge cases such as expired sessions and partial onboarding.
- Define where session validation happens, where claims are trusted, and where database lookups remain required.

## Apply Decision Rules

- Authentication answers “who are you”; authorization answers “can you do this.”
- Frontend route guards are UX aids, not the security boundary.
- Every protected backend mutation requires server-side authorization checks.
- Use PKCE for public clients.
- Use CSRF protection for cookie-backed browser auth.
- Separate account recovery flows from normal login flows.
- Treat admin and support tooling as higher-risk than normal end-user paths.

## Output Requirements

Always include:

1. The recommended auth/session model.
2. The authorization model and permission boundaries.
3. The trust assumptions and threat-sensitive areas.
4. The main security risks and how to mitigate them.
5. Required route, API, and storage protections.
6. User-flow handling for login, logout, expiry, onboarding, and recovery.
