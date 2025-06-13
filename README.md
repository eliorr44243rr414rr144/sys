# infra-ops-event-pipeline

*(ops / GitHub Enterprise — Internal Repository)*

---

Internal pipeline for ingesting and processing Roblox infrastructure events and operational telemetry.  
Supports observability, compliance, and auditability across datacenters and services.

---

## Overview

The **Infra Ops Event Pipeline** processes large-scale internal operational telemetry and event streams across Roblox infrastructure.

Key pipeline functions:

- Ingest internal infra events from Kafka (`ops-ingestion-events`, `ops-infra-events`).
- Normalize and enrich event metadata.
- Write processed data to Infra Data Warehouse and long-term audit log.
- Provide real-time metrics and alerting for operational visibility.

---

## Architecture

- **Ingestion:** Kafka → InfraEventPipeline
- **Processing:** Normalization, enrichment, schema enforcement
- **Storage:** DW → `infra_events_prod` + S3 → `infra-audit-archive-prod`
- **Observability:** Grafana dashboards, Datadog metrics, Slack & PagerDuty alerts

See [docs/architecture_overview.md](docs/architecture_overview.md) for full architecture details.

---

## Development

### Running Tests

```bash
pytest tests/
```

### CI Validation

```bash
python scripts/ci/validate_config_pipeline_structure.py
python scripts/ci/validate_config_stage_definitions.py
```

### Deploying Pipeline

Deploy via [GitHub Actions workflow](.github/workflows/deploy.yml).

---

## Compliance

- GDPR compliance supported via DSR pipeline.
- Audit logs retained 730 days per [docs/audit_compliance.md](docs/audit_compliance.md).

---

## Contacts

- Infra Platform team → infra-platform@roblox.com
- Compliance team → compliance-team@roblox.com
- Legal-ops → legal-ops@roblox.com

---

© Roblox Corporation Internal Use Only.