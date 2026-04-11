# Architecture Checklists

## Boundary Review

- Identify domain logic vs transport vs infrastructure.
- Identify circular dependencies.
- Identify high-churn modules.
- Identify shared modules with unclear ownership.
- Identify places where private internals are imported through side doors.

## Split Decision

- Does the code have a different owner?
- Does it need a different release cadence?
- Does it need a different scaling profile?
- Does it need failure isolation?
- Would splitting it improve or worsen operational overhead?

## Migration Planning

- isolate interface first
- move reads before writes when practical
- move tests with ownership
- keep old and new paths measurable
- remove dead paths quickly after cutover
