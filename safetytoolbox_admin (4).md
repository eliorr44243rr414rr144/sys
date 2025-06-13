# SafetyToolbox — Admin Tips & Current Practices

*Last updated: 2025-06-12 • Maintainers: SafetyToolbox Leads / Safety Infra Oncall*\
*Last full review: 2025-05-15 → post SAFE-1427 review in progress → SAFE-1444 tracking*\
*This document is a ****living resource****, not a formal playbook. For SEV2+ workflows, use the Incident Playbook → *[*SAFE-1598*](https://jira.rbx.com/browse/SAFE-1598)*.*

---

## ⚠️ If you are reading this because:

✅ You are on Safety Infra Oncall → this is your baseline.\
✅ You are a TS Ops Lead triaging stuck cases → good → cross-check `#safety-infra-oncall`.\
✅ You are Legal reviewing an audit export → see Audit Completeness Matrix.\
✅ You are in SEV2+ → STOP → use Incident Playbook → [SAFE-1598](https://jira.rbx.com/browse/SAFE-1598).\
✅ You are a new Lead → read this full doc prior to first rotation shift.

---

## Meta / TODO

- This is NOT a playbook → **shared internal best-practices + operational tips** → Leads + Infra maintain this.
- Last fully verified: May 2025 → post SAFE-1427 review WIP → SAFE-1444.
- Audit DLQ → batch → stream migration blocked → SAFE-1324.
- StuckCaseDetection tuning → noisy post deploy → SAFE-1879.
- Classifier v5 audit validation → pending post SAFE-1427 → SAFE-1442.
- FeatureFlags audit feed → blocked on FeatureCtl 4.2 → SAFE-1532.
- Infra priority → audit clarity **over system speed**.
- Legal priority → full flag traceability **over UX flow speed**.
- Known gap → AuditFeed export → IRR inconsistencies → SAFE-1221 (legacy).

---

## Admin Principles

✅ **Audit first** → *if it’s not in the audit, it didn’t happen*.\
✅ **Moderator safety second** → preserve clear escalation clarity → avoid clever hacks.\
✅ **System stability third** → don’t destabilize SafetyToolbox → prefer slower correct actions.\
✅ **Cross-team comms** → don’t surprise Legal, Infra, TS Ops.\
✅ **Escalate first → act second** → Infra / Leads aligned on this.

---

## Key Links

- [SafetyToolbox Main](https://tools.simulprod.com/)
- [SafetyToolbox Admin](https://tools.simulprod.com/admin) → NOTE: Admin v2 → migrating to Admin v3 → SAFE-1403.
- [Queue Control](https://tools.simulprod.com/admin/queue_control)
- [Manual Flag Tools](https://tools.simulprod.com/admin/manual_flag_tools) → staging only → prod triggers Infra alert.
- [Audit Trail Viewer](https://tools.simulprod.com/admin/audit_viewer) → DLQ gaps → SAFE-1532.
- [Classifier Info](https://tools.simulprod.com/admin/classifier_info) → caching lag (~15 min).
- [Staging Env](https://tools.simulprod.com/staging)
- [Staging Hash Search](https://tools.simulprod.com/staging/hash_search)
- [SAFE Project Jira](https://jira.rbx.com/projects/SAFE/summary)
- [SafetyToolbox Service Catalog](https://services.rbx.com/catalog/safetytoolbox)

---

## SAFE Jira Tags Reference Matrix

| Tag Name              | When to Use                          | Required In |
|-----------------------|--------------------------------------|-------------|
| LEGAL_PRIORITY        | Any export involving flagged CSAM    | SAFE Jira Issues |
| AUDIT_GAP             | When audit event is missing or incomplete | SAFE Jira Issues |
| SEV2                  | All SEV2 incidents                   | SAFE Jira SEV tracking |
| SEV3                  | All SEV3 incidents                   | SAFE Jira SEV tracking |
| FLAG_ROLLOUT          | All FeatureFlag rollouts impacting Prod | SAFE FeatureFlag tracking |
| POSTMORTEM_REQUIRED   | Any SEV requiring full Postmortem     | SAFE Jira Postmortem Issues |

---

## Escalation Slack Channels Matrix

| Purpose                                | Slack Channel Name             | Notes |
|----------------------------------------|-------------------------------|-------|
| SEV2 / SEV3 General Escalation         | `#safety-infra-oncall`        | Primary Infra Oncall channel |
| Legal Escalation (CSAM / Legal Export) | `#safety-legal-oncall`        | Legal oncall escalation |
| Leads Escalation                       | `#safety-mod-leads`           | TS Ops Leads + Legal coverage |
| Classifier Rollout / Issues            | `#safetytoolbox-engineering`  | FeatureFlag rollout and issues |
| AuditFeed Ingest / DLQ Monitoring      | `#safety-infra-oncall`        | Also flagged via PagerDuty |
| SEV Retrospective Review               | `#safety-sev-retrospective`   | Used for SEV Postmortem reviews |

---

