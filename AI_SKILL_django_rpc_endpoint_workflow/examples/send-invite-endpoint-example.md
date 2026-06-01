# Send Invite Endpoint Example

## Route
`POST /api/team/send-invite/`

## Why RPC Fits
The endpoint triggers a discrete action rather than representing a standalone resource update.

## Boundary
- View: auth, payload validation, team ownership
- Service: invite creation, dedupe, email dispatch

## Retest
Repeat the same request and confirm duplicate invites are handled intentionally.
