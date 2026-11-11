# 01 — Business Understanding

## Decision context

The scenario asks an analyst to design Power BI reports for three audiences at fictional **Aurora University**. The assignment presents a need for stronger, audience-specific decision-making across academic affairs, facilities and administration. It does not document a measured failure of an existing production system, so statements about current system fragmentation or historical losses would be unsupported.

**Portfolio reframing:** rather than treating dashboards as the end product, treat them as a proposed **decision-support capability** with three related workstreams.

## Decision problem and objective

> **Problem:** How can faculty, department leaders and admissions administrators interpret relevant operational signals consistently and decide which issues need further investigation or intervention?

**Objective:** specify and demonstrate role-specific reporting that provides valid, interpretable measures and a path from the signal to a responsible next action.

| Role | Priority decision | What a useful report must clarify | Proposed downstream action |
|---|---|---|---|
| Faculty member | Where might students need learning support? | GPA distribution, pass rate, attendance, course comparison, valid denominators | Review course-level support and assessment data before interventions |
| Department head | Which maintenance issues create an operational risk? | Work-order backlog, overdue cases, cost, priority, satisfaction feedback | Review overdue/high-priority work orders and resource constraints |
| Administrative officer | Which groups may benefit from support or service-process review? | Entry channel mix, observed current academic risk, participation, cohort sizes | Audit support processes and examine whether follow-up assistance is needed |

## Scope and boundaries

**In scope:** definition of management questions; stakeholder-specific requirements; dashboard specifications; illustrative metric logic; quality checks; interpretation; responsible decision rules; validation and proposed rollout.

**Out of scope:** functioning university enterprise integration; identifying named students; predicting dropout before admission; assessing staff performance from thin evidence; claiming that synthetic data captures actual campus operations.

## Success criteria (proposed, not achieved)

1. Each report has a named owner and answers at least one actionable management question.
2. Metrics define population, grain, calculation, snapshot date and missingness treatment.
3. Cross-filtering and drill-down never change denominators silently.
4. Stakeholders can correctly interpret the indicators and explain one appropriate next action in a scripted UAT scenario.
5. Sensitive segmentation is subject to role-based access and fairness/privacy review.
6. Changes to operational KPIs can be monitored after a controlled pilot; reporting alone is not counted as business impact.

## Stakeholders and constraints

**Primary:** faculty members, department heads, admissions/student support administrators. **Supporting:** data owners, BI developers, privacy/security staff, institutional leadership and affected students.

The original assignment supplies a fictional organisation and generated/sourced scenario data, not confirmed stakeholder interviews. Requirements below are therefore **proposed portfolio requirements**, not documented statements from real Aurora users.

### Evidence and uncertainties

- The submitted report's introduction and dashboard sections support these three target audiences.
- Actual source-system ownership, data refresh arrangements, consent basis, SLAs and integration architecture are **not specified** in the assignment.
- Strong performance claims require a validated data model, not just attractive screenshots.

[Next → Stakeholder requirements](02-stakeholder-requirements.md)
