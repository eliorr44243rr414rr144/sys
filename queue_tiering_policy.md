# Queue Tiering Policy

Infra Ops Event Pipeline queues are tiered to optimize processing and resource utilization.

| Tier | SLA Target | Priority |
|------|------------|----------|
| Tier1_Critical | 10 min | High |
| Tier2_HighPriority | 1 hr | Medium |
| Tier3_Backlog | 4 hr | Low |

## Routing Rules

- Critical alerts → Tier1_Critical
- Compliance processing → Tier2_HighPriority
- Backlog data ingestion → Tier3_Backlog

Tiering policy reviewed quarterly.