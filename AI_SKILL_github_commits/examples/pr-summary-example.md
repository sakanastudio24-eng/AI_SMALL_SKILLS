# PR Summary Example

## Intent

Split session expiry enforcement from unrelated UI cleanup so the auth fix can be reviewed and reverted independently.

## Risks

- protected-route middleware changed
- existing tests cover happy path only

## Reviewer Focus

- expiry behavior on protected routes
- redirect behavior after session timeout
