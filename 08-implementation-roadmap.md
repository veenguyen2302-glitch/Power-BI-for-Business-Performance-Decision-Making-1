# 08 — Proposed Implementation and Measurement Roadmap

The original coursework delivered dashboard prototypes/reports, not a confirmed deployed BI platform. This page is a **future-state proposal**, not a record of implementation.

| Phase | Work | Exit gate | Accountable role (proposed) |
|---|---|---|---|
| 0 — Discover | Confirm data owners, decisions, audience, privacy and KPI definitions | Approved scope and data contracts | Business sponsor + BI analyst |
| 1 — Audit | Review source tables, joins, missingness, refresh cadence and current dashboard measures | Valid reconciliation and source trust | Data owner + analyst |
| 2 — Correct | Replace misleading aggregations and titles; design required measures and drill paths | Technical unit tests / chart review | BI developer |
| 3 — Pilot | Small, permissioned audience tests each report and decision scenario | UAT sign-off and privacy review | Business owner + governance |
| 4 — Operate | Refresh, alert ownership, monthly KPI review and decision-log monitoring | Defined runbook and incident path | Report owner |
| 5 — Evaluate | Compare pilot decisions/outcomes to agreed baseline and control/comparison where feasible | Evidence-supported continuation decision | Sponsor + evaluation lead |

## Dependencies

- Original complete fact tables and stable data extracts (not supplied here).
- Approved refresh and metric ownership.
- Access controls / student confidentiality agreement.
- Corrected Power BI visuals validated against independent calculations.
- Agreed intervention and value-measurement methodology.

## Risks and mitigations

| Risk | Why it matters | Proposed mitigation |
|---|---|---|
| Synthetic-data assumptions treated as reality | Misleading recommendations | Label evidence, test against real sources only with approval |
| Aggregation/axis errors | Incorrect management decisions | Metric dictionary, independent reconciliations and peer review |
| Selection bias in student groups | Misleading group comparisons | Confounder review, minimum sample thresholds, no causal claims |
| Identity-based student treatment | Fairness and discrimination concerns | Needs-based support, privacy review, aggregate monitoring |
| Stale reports | Incorrect operational action | Show refresh time, owner and data quality status |
| Alert overload | Staff time wasted | Pilot thresholds and monitor precision/actionability |

## Definition of done for a real rollout (not yet met)

Validated source data, signed-off requirements, corrected KPI calculations, permissioned access, passing technical tests, formal UAT, named metric owners, incident/refresh runbook and evaluated pilot outcomes.

[Next → Evidence and limitations](09-provenance-and-limitations.md)
