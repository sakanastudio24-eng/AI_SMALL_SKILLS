# AI_SKILL_endpoint_health_auditor

## Purpose
Handle endpoint and subdomain health checks safely across DNS, TLS, HTTP, and health-route coverage issues.

## Use When
- checking whether services respond
- validating health endpoints
- diagnosing TLS or connectivity failures
- reviewing failing dependencies
- producing remediation steps for unhealthy services

## Do Not Use When
- building unrelated application features
- doing architecture planning without live endpoint concerns
- making frontend-only UI changes

## Inputs Needed
- target URLs or subdomains
- expected health route if known
- timeout or environment constraints
- whether machine-readable output is needed
- ownership or escalation context

## Steps
1. Collect explicit targets.
2. Run the checker script or inspect target health behavior.
3. Classify the failure bucket.
4. Identify the missing health route or failing dependency.
5. Recommend the next operational step.

## Output
- endpoint status summary
- root-cause bucket
- remediation guidance
- edge-case checklist

## Constraints
- prefer HTTPS when possible
- distinguish DNS, TLS, network, HTTP, and app-layer failures
- do not claim an endpoint is healthy without a real 2xx health response
- health changes require manual review before shipping

## Related Skills
- AI_SKILL_system_design
- AI_SKILL_web
- AI_SKILL_github_commits
