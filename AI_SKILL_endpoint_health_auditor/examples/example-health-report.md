# Example Health Report

## Target

`https://api.example.com`

## Result

- status: `health_endpoint_missing`
- root-cause bucket: `http`
- evidence: host responds on `/` but common health routes return `404`

## Next Step

Add `/healthz` or `/readyz` and include dependency checks appropriate for the service.
