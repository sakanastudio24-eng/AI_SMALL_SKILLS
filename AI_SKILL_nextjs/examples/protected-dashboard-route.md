# Protected Dashboard Route Example

## Structure

- `app/dashboard/layout.tsx` checks session boundary
- `app/dashboard/page.tsx` renders server-fetched data
- client components handle only interactive widgets

## Rule

Do not push auth checks into random client components when the route boundary can handle them.
