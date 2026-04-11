# Endpoint Health Auditor Checklist

## Pre-ship
- [ ] Target URLs are correct
- [ ] Health route is checked or marked missing
- [ ] TLS status is verified
- [ ] Failure bucket is identified
- [ ] Next step is actionable

## Edge Cases
- [ ] DNS resolution failure
- [ ] TLS handshake or expiry issue
- [ ] Host responds but no health route exists
- [ ] Endpoint returns intermittent 5xx
- [ ] Timeout or blocked network path
