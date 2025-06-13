# Observability Best Practices

## Metrics

- Every pipeline stage must emit:
    - Latency p95
    - Error rate
    - Throughput

## Logging

- Logs must include trace ID.
- Logs must be structured (JSON).

## Alerting

- Alerts must have runbook link.
- Alerts must include Slack + PagerDuty notification.

## Dashboards

- Required dashboards:
    - Pipeline latency / error rate
    - Kafka consumer lag
    - Deployment health

## Notes

- Observability reviewed monthly.