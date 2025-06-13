# Recovery Playbook

## Common Failures

| Failure | Action |
|---------|--------|
| Kafka lag spike | Increase consumer concurrency, check broker health |
| Pipeline stage crash | Roll back deploy, check stage logs |
| DW ingest failure | Investigate staging table load process |

## General Steps

1. Identify root cause.
2. Execute targeted recovery action.
3. Validate recovery via dashboards.
4. Document in postmortem.

## Communication

- Post updates in `#infra-oncall`.
- Notify stakeholders as needed.