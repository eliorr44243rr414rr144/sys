# Audit Compliance

## Retention Policy

- InfraAuditPolicy.xml → 730 days retention for `OpsPipelineActions`
- S3 Archive → `infra-audit-archive-prod`

## Sensitive Actions

- PipelineConfigChange
- ProductionDeployment
- SchemaMigration

## Audit Trail Fields

- `LastModifiedBy`
- `LastModifiedAt`
- `ChangeReason`

## Compliance Contacts

- compliance-team@roblox.com
- legal-ops@roblox.com
- security-audit@roblox.com

## Process

- All pipeline config changes auto-logged
- Deployments auto-logged via CI/CD
- Audit log viewer restricted to Infra Platform SRE + Compliance

## Notes

- GDPR compliance supported → audit data deletions handled via DSR requests
- Periodic review of audit policy every 6 months