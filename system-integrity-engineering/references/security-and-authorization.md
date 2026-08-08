# Security And Authorization

Use this reference for authentication, authorization, ownership, privileged roles, route protection, RLS, server-only boundaries, object access, or sensitive data handling.

## Separate Concepts

Always distinguish:

- authentication
- authorization
- visibility
- data classification
- ownership
- workflow state

The fact that a user can see a button, route, or cached record does not authorize the mutation.

## Review Targets

Check:

- direct endpoint access
- server-only boundaries
- caller-selected actor IDs
- privilege escalation
- insecure defaults
- object-level authorization
- role changes
- stale sessions
- cached authorization
- privileged database functions
- grant boundaries
- input validation
- output minimization

## Authority Rules

- Enforce authorization server-side or at the authoritative data boundary.
- Do not trust frontend role state for consequential writes.
- Do not accept caller-supplied owner, tenant, user, or staff IDs without deriving or validating them server-side.
- Minimize returned fields.
- Avoid privileged keys in browser, mobile, or extension code.
- Treat hidden routes as still publicly callable unless protected.

## Security Test Requirements

For protected behavior, include at least:

- allowed actor succeeds
- unauthenticated actor fails
- wrong owner fails
- wrong role fails
- stale or revoked session fails where applicable
- direct endpoint call is covered, not just hidden UI

State which evidence level proves each claim.
