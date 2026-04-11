# Mobile Login Flow Example

1. User opens sign-in screen.
2. User picks email or provider login.
3. App shows loading state during auth.
4. Callback or deep link returns to the app.
5. Session is established and the user lands on the intended screen.

## Edge Cases

- interrupted login returns to sign-in with useful feedback
- expired session redirects to sign-in without losing context when possible
