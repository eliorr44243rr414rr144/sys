# Metrics & Alerting Guide

## Key Metrics

- `infra_pipeline_latency_p95_ms`
    - Target: < 2000ms
- `infra_pipeline_error_rate_percent`
    - Target: < 0.5%
- Kafka topic lag (`ops-ingestion-events`)

## Dashboards

- [Infra Pipeline Metrics - West](https://metrics.rbx.com/d/infra_pipeline/infra-pipeline-west)
- [Infra Pipeline Metrics - East](https://metrics.rbx.com/d/infra_pipeline/infra-pipeline-east)

## Alerting Channels

- Slack: `#infra-oncall`
- PagerDuty Service: `Ops-Infra Pipeline`

## Alert Thresholds

| Metric | Threshold | Action |
|--------|-----------|--------|
| Latency p95 | >2000ms | Investigate Kafka lag / processing bottlenecks |
| Error rate | >0.5% | Investigate errors, check DLQ |
| Kafka topic lag | >1M messages | Investigate Kafka brokers / consumer group lag |

## Notes

- All alerts automatically routed to Oncall
- PagerDuty overrides for major events