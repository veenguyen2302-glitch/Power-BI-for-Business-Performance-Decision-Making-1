# 04 — Analytical Findings and Interpretation

## Interpretation rule

The original report contains descriptive findings, but the independent source tables behind its three dashboards have not been provided for rerunning. Therefore, the first table below records **source-reported statements** rather than verified metrics. The demonstration results are a separate synthetic data layer.

## A. Original submission: reported observations (not independently reproduced)

| Workstream | Source-reported finding | What the evidence does **not** show |
|---|---|---|
| Faculty | The original dashboard displays average cumulative GPA **3.10**, pass rate **97.65%**, average attendance **70.58**. The report identifies lower average GPA in Economics and Business Law than in several other courses. | No causal demonstration that study effort, course content or scholarships explain the differences; some report visuals require aggregation audits. |
| Facilities | The report flags differing maintenance durations, costs and satisfaction patterns across departments and campuses, including examples with poor satisfaction. | No verified relationship between a site's maintenance spend and realised service improvement; some visual axes and measures require correction. |
| Administration | The report describes current risk group patterns, enrolment channels, scholarships and learning outcomes. The decomposition tree shows a reported **67 high-risk** records. | Risk is not necessarily known at admission; subgroup contrasts do not justify discriminatory targeting or intervention by nationality. |

Source: submitted *MIS781 Business Intelligence Solution Development and Report*, dashboard sections 2.1–2.3 and recommendations. These figures are historical coursework **report values**, not metrics from the reproducible demonstration.

## B. New reproducible demonstration — synthetic results only

The runnable analysis generates 650 entirely fictional student records, 650 course-result rows and 780 fictional maintenance work orders. It uses an invented current-term risk rule, not an empirical model. Metrics are output at runtime in `demo/outputs/portfolio_metrics.json` and CSV summaries.

- [Faculty breakdown](../demo/outputs/faculty_by_course.csv) and [chart](../demo/outputs/faculty_gpa.svg)
- [Facilities by work type](../demo/outputs/facilities_by_type.csv) and [chart](../demo/outputs/facilities_overdue.svg)
- [Current academic risk by enrolment channel](../demo/outputs/admissions_by_channel.csv) and [chart](../demo/outputs/admissions_risk.svg)

The synthetic patterns demonstrate the workflow and metric definitions. **They are not findings about real or original Aurora students.**

## C. Management interpretation

### Academic performance

A course below the university's reference GPA is a **triage signal**. Before intervention, verify course enrolment counts, grade definitions, assessment mix, time period and relevant support needs. The next decision is whether to conduct a targeted learning review, not to assign blame.

### Maintenance

A high overdue rate is a **workflow signal**. Reconcile open versus completed cases, assess severity and whether apparent delays reflect resource shortages, vendor constraints, scope changes or missing completion dates. Select a prioritised backlog review before deciding on spend changes.

### Administration

A channel-level difference in observed post-term risk is a **review signal**, not proof that an acquisition channel causes later outcomes. Compare populations, support provision and prior academic context; avoid individual decisions based on nationality or other sensitive characteristics.

## D. Distinguish decision evidence from impact

- Observing a dashboard metric **does not** establish that an intervention improved it.
- An association between scholarships and attendance **does not** establish scholarship effectiveness.
- Demonstrating a correct SQL calculation **does not** make an invented dataset representative.

A real pilot would require a baseline, owner, intervention protocol, comparable group or other suitable evaluation design, and post-intervention data collection.

[Next → Dashboard design](05-dashboard-design.md)
