# 02 — Stakeholder Requirements and Traceability

The original MIS781 submission developed three stakeholder-facing BI dashboards. The following structured requirements and acceptance criteria are **new portfolio enhancements**, designed to make the management decisions testable.

## Stakeholder needs to measurable requirements

| ID | User story / decision need | Acceptance criterion | Evidence | Priority |
|---|---|---|---|---|
| R-01 | As a **faculty member**, I want to compare average GPA and pass rate by course so I can identify subjects warranting review. | Metric dictionary states the pass definition, scale, record grain and total eligible results; filters do not double-count. | Faculty screenshot and demo SQL | Must |
| R-02 | As a **faculty member**, I want to see attendance and study effort alongside outcomes without implying causality. | Charts label aggregation, sample size and time period; accompanying text uses **associated with**, not **caused by**. | Academic dashboard / interpretation note | Should |
| R-03 | As a **department head**, I want an overdue work-order view by type and department to prioritise operational follow-up. | Overdue status uses a fixed snapshot date; totals reconcile to one row per work order. | Facilities chart and demo query | Must |
| R-04 | As a **department head**, I want to compare cost, urgency and satisfaction, not conflate duration with delay. | Units and titles match actual axes; priority displayed using a suitable distribution or average, not `SUM(priority)` labelled as average. | Source audit and corrected design | Must |
| R-05 | As an **administrator**, I want to identify current support needs by cohort and entry channel. | Risk definition is clearly **post-term descriptive**; counts/rates have visible denominators; low-N groups can be suppressed. | Admissions demo and risk logic | Must |
| R-06 | As a **privacy/data owner**, I want all reports to respect access and ethical-use limits. | Demonstration uses no personal data; any future real deployment has role-based access, retention rules and fairness review. | Data governance requirements | Must |
| R-07 | As a **BI owner**, I want failed data checks to block publication so users are not misled. | Duplicate keys, invalid ranges, orphaned joins and invalid chronology cause the reproducible pipeline to fail. | `demo/sql/03_validation.sql` and tests | Must |
| R-08 | As a **management sponsor**, I want action and impact measures linked to dashboard findings. | A proposed intervention specifies owner, baseline, leading/lagging KPIs and evaluation design. | Decision playbooks | Should |

**Priority note:** MoSCoW ratings in this table are portfolio recommendations, not evidence of stakeholder sign-off.

## Traceability matrix

| Problem / decision | Requirement | Dataset / grain | Output | Proposed test |
|---|---|---|---|---|
| Weak visibility of course outcomes | R-01, R-02 | `student_results` / course result | Faculty summary and course chart | T-01, T-02 |
| Inconsistent maintenance triage | R-03, R-04 | `work_orders` / work order | Overdue and cost overview | T-03, T-04 |
| Support planning needs defensible segmentation | R-05, R-06 | `students` / enrolled student + `student_results` | Channel/term result view | T-05, T-06 |
| Misleading or unreliable reporting | R-07, R-08 | All domains | Quality checks and decision framework | T-07, T-08 |

## Non-functional considerations

- **Interpretability:** clear units, time periods, denominators and caveats; colour is never the only carrier of meaning.
- **Reliability:** documented business rules; explicit refresh/snapshot date; failing validation checks stop publication.
- **Security:** no unrestricted exposure of row-level student information; role-based access is required before deployment.
- **Performance:** for a real deployment, agree refresh frequency and acceptable dashboard interaction latency with data owners; neither is verified by the assignment.
- **Auditability:** retain metric definitions and version-controlled changes to queries/visuals.

[Next → Data model and quality](03-data-model-and-quality.md)
