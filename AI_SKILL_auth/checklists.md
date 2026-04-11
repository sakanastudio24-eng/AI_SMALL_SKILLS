# Auth Checklist

## Pre-ship
- [ ] OAuth redirect URLs are correct
- [ ] Magic link callback works
- [ ] Session persists after refresh
- [ ] Expired links fail gracefully
- [ ] No secrets are exposed
- [ ] Server-side authorization checks exist for protected actions

## Edge Cases
- [ ] Invalid token
- [ ] Used magic link
- [ ] Missing session
- [ ] Wrong redirect target
- [ ] Revoked or expired session
