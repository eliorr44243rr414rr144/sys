# Alert Routing

## Alert Channels

| Alert Type               | Channel / Target       |
|--------------------------|------------------------|
| P1 Pipeline Latency      | PagerDuty: Ops-Infra Pipeline |
| P1 Pipeline Error Rate   | PagerDuty: Ops-Infra Pipeline |
| Kafka Topic Lag          | Slack: #infra-oncall   |
| Deployment Failures      | Slack: #infra-deploys  |
| Compliance Issues        | Slack: #compliance-team |

## Notes

- All alerts must include link to runbook.
- Alerts must be actionable.

## Escalation

- Oncall → Infra Platform SRE.
- Escalation path → Ops Engineering Manager.