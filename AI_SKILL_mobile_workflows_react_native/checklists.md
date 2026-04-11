# Mobile Workflows React Native Checklist

## Screen QA Checklist
- [ ] Screen purpose is obvious
- [ ] Touch targets are usable
- [ ] Layout works on realistic device sizes
- [ ] Loading, empty, and error states exist
- [ ] Navigation actions are predictable

## Auth-on-Mobile Checklist
- [ ] Session persists correctly
- [ ] Resume-from-background behavior is handled
- [ ] Interrupted auth flows recover safely
- [ ] Logout or session expiry returns to the right screen
- [ ] Deep links or auth redirects behave correctly

## Responsive / Device Checklist
- [ ] Small devices are usable
- [ ] Long content scrolls correctly
- [ ] Keyboard behavior is handled
- [ ] Platform-specific differences are reviewed
- [ ] Offline or weak-network states are considered

## Animation Sanity Checklist
- [ ] Animations support the flow
- [ ] Motion does not delay core actions
- [ ] Screen transitions feel intentional
- [ ] Gesture behavior is predictable
- [ ] Reduced-complexity behavior exists where needed
