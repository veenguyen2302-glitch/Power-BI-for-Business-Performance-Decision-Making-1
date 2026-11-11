# 09 — Source Audit, Provenance and Claim Boundaries

## Source inventory reviewed

| Artifact | Scope verified | Publication status |
|---|---|---|
| MIS781 individual report (23 pages) | Background, assumptions, role-specific dashboards, commentary and recommendations | Original report kept outside public repo due personal metadata/student ID; relevant dashboard screenshots reproduced as evidence |
| `Dashboard 1 - Faculty.pbix` | Faculty report visual layout and report structure | Retained privately pending privacy and Power BI compatibility review |
| `dashboard 2.pbix` | Facilities report visual layout and report structure | Retained privately pending review |
| `dashboard 3.pbix` | Admissions report visual layout and report structure | Retained privately pending review |
| `AuroraUniversity_Departments_50_EN.xlsx` | 50-row department lookup (ID/name/head columns) | Only ID/name reference fields included in synthetic demo; department-head names excluded |
| MIS781 A2 assignment brief | Requires three role-specific dashboards, four visuals each, interpretation and recommendations | Referenced, not reproduced |
| Portfolio synthetic generator and SQL | New illustrative data, calculations and automated checks | Included; reproducible using Python standard library and SQLite |

The original brief explicitly identifies the scenario names as fictional; raw data may be artificial or sourced. The report notes that data are derived from publicly available sources and/or GenAI; the complete original fact tables were not separately provided.

## Specific review findings

The supplied Power BI files were inspected at the report-layout level (read-only). The following differences should be resolved inside the BI tool before claiming validated metrics:

| Finding | Source evidence | Why it matters | Proposed correction |
|---|---|---|---|
| Course GPA chart appears to reference `Sum(...Cuml_GPA)` | Faculty PBIX visual query metadata | Sum grows with class size, not academic performance | Replace with documented `AVERAGE` or agreed student-weighted GPA |
| Priority radar appears to reference `Sum(...Priority)` | Facilities PBIX visual query metadata | Summed scores reflect work-order volume | Use priority distribution/valid mean, with case count |
| Satisfaction heatmap appears to reference `Sum(...SatisfactionScore)` | Facilities PBIX visual query metadata | Sum is not average satisfaction and is sensitive to response volume | Average valid scores and display response N / coverage |
| Scatterplot title refers to **Delay Days**, but x-axis references `Duration` | Facilities PBIX visual query metadata | Duration and lateness are different metrics | Align axis and title, or calculate delay from dates |
| Report discusses scholarship **impact** and course effects from descriptive patterns | MIS781 written narrative | No causal identification | Change to association and propose an evaluation design |
| Risk comparisons by nationality in synthetic admission scenario | Original report | Weak policy basis, fairness and representativeness risks | Remove identity-based individual decisions; require governance review |
| Original source datasets not fully available | Upload inventory | Cannot independently reproduce original numeric KPIs | Retain as **reported**, not revalidated; use a separate illustrative demo |
| Template remnants and figure-caption inconsistencies | MIS781 Word report | Reduces professional presentation quality | Use newly written portfolio pages; do not upload the unedited report |

## Claims appropriate for CV and interviews

**Supported:** developed three Power BI dashboards for different decision audiences in an academic scenario; interpreted role-relevant data; proposed recommendations; later created a reproducible SQL/Python demonstration and audit of reporting definitions.

**Unsupported:** worked for a real Aurora University, interviewed actual university leadership, deployed reports into production, improved grades or enrolments, saved money, proved a scholarship effect, or independently confirmed original reported figures from raw records.

## Ethical and privacy practices

- The public demonstration uses fictional `AU-ST` identifiers and no contact details or names of students.
- The source department spreadsheet includes head names; the public demo intentionally excludes them.
- Avoid risk labelling based on nationality or any other identity group. Aggregate comparisons should have a documented purpose, confidentiality protections and fairness review.
- Do not publish original `.pbix` files until checking embedded data, metadata, connection strings and rights to distribute the source content.

[Back to README](../README.md)
