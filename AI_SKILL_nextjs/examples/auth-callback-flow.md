# Auth Callback Flow Example

1. Provider returns to `/auth/callback`.
2. Route handler validates callback params.
3. Server establishes session.
4. User is redirected to the intended protected route.

## Notes

Keep callback logic explicit and keep redirect behavior easy to trace.
