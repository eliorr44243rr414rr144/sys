# Secrets Management Guide

Infra Ops Event Pipeline adheres to strict secrets management practices.

## Storage

- Secrets stored in Roblox Vault.
- Access controlled via RBAC.

## Rotation Policy

| Secret Type | Rotation Frequency |
|-------------|--------------------|
| Database credentials | 90 days |
| API tokens | 60 days |
| Service certificates | 180 days |

## Access Monitoring

- Access logs audited weekly.
- Alerts configured for anomalous access patterns.