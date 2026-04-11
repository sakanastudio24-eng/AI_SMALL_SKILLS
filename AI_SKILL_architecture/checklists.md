# Architecture Checklist

## Pre-ship
- [ ] Module boundaries are explicit
- [ ] Dependency direction is clear
- [ ] Circular dependencies are addressed
- [ ] Ownership lines are documented
- [ ] Migration path is incremental

## Edge Cases
- [ ] Shared module absorbs volatile business logic
- [ ] Service split adds more ops cost than value
- [ ] Legacy path remains partially active
- [ ] Tests still depend on old boundaries
- [ ] Ownership is unclear after refactor
