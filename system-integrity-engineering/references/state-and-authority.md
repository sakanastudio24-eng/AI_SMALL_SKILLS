# State And Authority

Use this reference for workflow state, UI state, cached state, state machines, route state, concurrent requests, authorization boundaries, and source-of-truth decisions.

## State Ownership

Every stateful workflow must declare:

- authoritative state owner
- derived projections
- local UI state
- URL state
- cached state
- transition initiator
- mutation authority
- reconciliation rules
- stale-response protection
- terminal states

There must be one clear owner of each state.

## Stale Transition Guard

Protect against:

```text
Request A begins
User selects B
Request B completes
Request A completes late
A incorrectly overwrites B
```

Valid techniques include request identity, sequence tokens, cancellation, selected-reference comparison, and reducer-owned transitions.

## Authority Rules

Frontend visibility is not authorization. Backend authorization must be enforced directly. Database authority must not be replaced by cached UI state.

Rules:

- The UI may project available actions.
- The server must validate the action at mutation time.
- The database or authoritative service must preserve ownership rules.
- A cached projection cannot decide a consequential write.

## State Machine Review

For each transition, identify:

- from state
- event
- actor
- authorization check
- mutation owner
- success state
- failure state
- retry behavior
- stale response behavior
- diagnostic code

If a state can be terminal, make further writes explicitly impossible or idempotent.
