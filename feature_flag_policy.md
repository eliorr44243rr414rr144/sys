# Feature Flag Policy

Feature flags enable safe staged rollouts of new features.

## Guidelines

- All new features must be flag-gated.
- Flags default to OFF.
- Rollouts staged (5%, 25%, 50%, 100%).

## Ownership

| Flag | Owner |
|------|-------|
| metrics_latency_target_ms | infra-platform@roblox.com |
| enable_gdpr_audit_logging | compliance-team@roblox.com |

## Expiry

Flags reviewed quarterly; stale flags removed.