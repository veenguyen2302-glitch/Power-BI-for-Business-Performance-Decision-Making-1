# 10 — Recruitment Story and Interview Walkthrough

## Portfolio title

**Aurora University | Stakeholder-Centred Business Intelligence and Operational Decision Support**  
*Deakin University academic scenario; subsequently extended into a reproducible analytics portfolio.*

## CV bullets — choose 2–3 and adapt to the job description

- Developed **three role-specific Power BI reports** for a university business case, translating faculty, facilities and admissions needs into KPI-driven views and management recommendations.
- Analysed academic performance, maintenance operations and enrolment engagement patterns, presenting insights for distinct decision-makers while recognising data and causality limitations.
- Extended the project into a **reproducible Python/SQLite analytics demonstration**, documenting metric definitions, data relationships, seven automated quality checks and dashboard validation scenarios.
- Audited visual configurations for **aggregation and label consistency**, identifying improvements to GPA, satisfaction, priority and maintenance-duration measures to strengthen decision reliability.

The last two bullets describe **new later portfolio work**, not tasks documented as part of the original university submission.

## 60-second interview pitch

> “For my Business Intelligence and Databases assessment, I developed three Power BI dashboards addressing different decisions at a fictional university: monitoring course performance, managing facilities and understanding admissions-related engagement. The key learning was that a dashboard needs to answer a decision question and use the right metric grain—not just display interesting charts. When I revisited the project for my portfolio, I audited measure definitions and found areas where aggregated GPA or satisfaction and mismatched chart labels could mislead users. I built a small reproducible synthetic data pipeline with SQL checks and documented acceptance scenarios to show how I would validate and operationalise the reporting in a real organisation. The dashboards themselves were academic prototypes, and I would still need real data-owner and stakeholder sign-off before production.”

## Five-minute walkthrough

1. **Context (30 sec):** Three functional teams, three different management decisions.
2. **Original work (60 sec):** Show the three Power BI screenshots and explain each audience's question.
3. **Technical challenge (60 sec):** Explain row grain and why summed GPA / satisfaction or duration vs delay are problematic.
4. **Reproducible follow-up (90 sec):** Show the synthetic generator, SQLite metrics, automated checks and interactive site.
5. **Action & limitations (60 sec):** Walk through one proposed decision playbook and describe how a real pilot would be evaluated.

## Questions to prepare for

- How did you decide what each stakeholder needed to see?
- What is the difference between a metric, KPI and business outcome?
- What happens when a dataset has one row per work order versus one row per department?
- How do you validate a Power BI chart independently?
- What is wrong with summing GPA or treating descriptive scholarship differences as causal effects?
- How would you handle small student groups and sensitive attributes?
- Which dashboard would you pilot first, and why?
- What additional evidence would you require before claiming the dashboard improved a business outcome?
