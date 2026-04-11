# Extension to Web Flow Example

1. User signs in on the website.
2. Extension detects account status through a safe bridge or backend lookup.
3. Popup shows linked-account status.
4. Content script enables page-specific actions only when the site and account state match.

## Risk

Avoid making the web account the only extension runtime source of truth unless the product explicitly requires it.
