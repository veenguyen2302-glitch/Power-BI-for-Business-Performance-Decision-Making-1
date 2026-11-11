# 05 — Dashboard Design for Management Decisions

## Design intent

The submitted assignment built three role-specific Power BI reports. The portfolio extends that work by specifying **what each dashboard should help someone decide**, how the measure is defined, and what diagnostic action follows a potential alert.

| Dashboard | User / priority | Lead indicators | Recommended interaction | Management action |
|---|---|---|---|---|
| Faculty | Educator reviewing student academic outcomes | GPA mean/distribution, pass rate, attendance by course | Filter by term/course, view eligible record count, drill into anonymised cohorts | Prioritise a course-support review |
| Facilities | Department head reviewing service reliability | Overdue %, priority bands, open backlog, costs, satisfaction coverage | Filter by campus, work type, department, period; open/closed toggle | Escalate high-priority overdue orders |
| Administration | Student services/admissions reviewing engagement | Channel counts, observed post-term support flags, attendance, scholarship breakdown | Cohort filter with privacy-safe aggregation and minimum-N rule | Review student support service pathways |

## Source screenshots

![Original faculty dashboard](../assets/faculty-original.png)
*Original faculty dashboard from the submitted report; needs metric and label verification.*

![Original facilities dashboard](../assets/facilities-original.png)
*Original facilities dashboard; its Cost vs Delay label and satisfaction/priority aggregation require review.*

![Original admissions dashboard](../assets/admissions-original.png)
*Original administration dashboard; ethnicity/nationality patterns should not be used as an individual risk policy.*

## Corrective design recommendations

### Faculty

- Replace course `SUM(GPA)` with a documented GPA mean and appropriate denominator.
- Present pass rate as a valid share, with an explicit rule for absence/withdrawal/missing grade.
- Replace ambiguous *scholarship impact* language with *scholarship-associated patterns*.
- Include sample sizes and a data completeness indicator.

### Facilities

- Align every axis to its title: **duration is not delay**. If plotting duration, change the title; if plotting delay, build a validated delay measure.
- Show work-order priority distributions or count by priority before claiming an average priority difference.
- Show `AVG(SatisfactionScore)` only among valid feedback responses and include response coverage.
- Separate overdue open orders from completed-late orders so users know what can still be acted on.

### Administration

- Define whether *risk* is an observed current-status flag or a genuinely prospective prediction.
- Add cohort sizes and suppress sensitive small cells.
- Avoid identity-based treatment; focus on transparent support eligibility and equitable access.
- Show metric time windows and known confounders before comparisons.

## Proposed review checklist

Every published visual must pass: **purpose → population → grain → calculation → units → filters → alternative explanation → next action**. This is the central design discipline of the portfolio.

[Next → Decision playbooks](06-decisions-and-interventions.md)
