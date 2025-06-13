# Oncall Runbook

## Goals

- Maintain availability of Infra Pipeline
- Respond quickly to alerts and failures
- Communicate impact to stakeholders

## Common Alerts

| Alert Name                          | Action |
|-------------------------------------|--------|
| infra_pipeline_latency_p95_ms > 2s  | Check Kafka lag, check enrichment services |
| infra_pipeline_error_rate_percent > 0.5% | Triage errors, check DLQ |
| InfraPipelineDeploymentFailed       | Rollback deploy, notify `#infra-deploys` |

## Standard Triage

1. Check Grafana dashboards → Infra Pipeline latency, errors
2. Check Kafka lag metrics → topic lag in `ops-ingestion-events`
3. Check deployment health → Kubernetes rollout status
4. Communicate impact → update `#infra-oncall`

## Escalation Path

- Primary Oncall → Infra Platform SREs
- Secondary Escalation → Ops Engineering Manager

## Notes

- PagerDuty: Ops-Infra Pipeline
- Slack: `#infra-oncall`, `#infra-deploys`