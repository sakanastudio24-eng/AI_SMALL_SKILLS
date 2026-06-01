# Expo Placeholder Integration Checklist

## Placeholder Boundary
- [ ] Temporary surface is named clearly
- [ ] Mock state is isolated
- [ ] Shared production logic is not polluted by temp behavior
- [ ] Replacement source is documented
- [ ] Removal path is obvious

## Flow Quality
- [ ] Navigation works end to end
- [ ] Loading, empty, and error states exist
- [ ] Back behavior is correct
- [ ] Device-size behavior is reasonable
- [ ] Temporary copy does not mislead users

## Replacement Readiness
- [ ] Data contract for future live source is noted
- [ ] Auth assumptions are explicit
- [ ] Screen dependencies are minimal
- [ ] Final implementation can replace the placeholder without wide rewrites
- [ ] QA caveats are documented
