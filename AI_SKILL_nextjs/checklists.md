# Next.js Checklist

## Route Structure
- [ ] route is placed in the correct app router location
- [ ] layout and page boundaries make sense
- [ ] route naming is clear

## Server vs Client
- [ ] client component is only used when needed
- [ ] server-side work is not pushed into client code unnecessarily
- [ ] browser-only APIs are isolated correctly

## Data Flow
- [ ] data fetching happens in the right place
- [ ] backend-touching logic is separated from UI
- [ ] loading and error states exist

## Auth / Protected Flow
- [ ] callback route works
- [ ] redirect behavior is correct
- [ ] protected routes behave correctly on refresh
- [ ] session handling is explicit

## Performance / Quality
- [ ] page is not overloaded with unrelated concerns
- [ ] initial load path is reasonable
- [ ] edge cases were reviewed
