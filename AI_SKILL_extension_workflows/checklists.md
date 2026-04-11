# Extension Workflows Checklist

## Extension Shipping Checklist
- [ ] Feature works across the intended extension surface
- [ ] Restricted pages are handled safely
- [ ] Runtime errors are visible and recoverable
- [ ] Host page behavior is not broken by the extension
- [ ] Ship-readiness notes are documented

## Permissions Checklist
- [ ] Requested permissions are minimal
- [ ] Host permissions are scoped narrowly
- [ ] Optional permissions are used where possible
- [ ] Permissions match actual runtime behavior
- [ ] No unnecessary long-term backend coupling exists

## Injection Checklist
- [ ] DOM assumptions are stable
- [ ] UI injection survives page refreshes or rerenders
- [ ] Overlay placement does not block host-page controls
- [ ] Cleanup occurs on navigation or teardown
- [ ] Injection is disabled on restricted or unsupported pages

## Runtime Debugging Checklist
- [ ] Popup/background/content-script message flow is clear
- [ ] Cross-tab behavior is tested
- [ ] Refresh and reconnect states are handled
- [ ] Disconnected or stale state is recoverable
- [ ] Error logs point to the failing surface
