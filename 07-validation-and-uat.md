# 07 — Acceptance, Reconciliation and UAT Plan

**Status: Proposed portfolio enhancement — no documented real stakeholder UAT execution.** The new synthetic pipeline has automated test results, but those checks do not replace stakeholder acceptance testing on real data.

## Proposed UAT scenarios

| Test ID | Requirement | Scenario | Expected result | Status |
|---|---|---|---|---|
| T-01 | R-01 | Select a course with multiple student results | Displays the **mean**, not sum, of GPA; record denominator and filter are correct | Planned |
| T-02 | R-02 | Compare grade and attendance categories | All values have units, N and the wording does not assert causality | Planned |
| T-03 | R-03 | Review an overdue work order | Completed-late vs open-overdue logic matches agreed reporting date | Planned |
| T-04 | R-04 | Review work-order priority and satisfaction | Priority scale and aggregation correct; satisfaction excludes missing responses and shows coverage | Planned |
| T-05 | R-05 | Filter observed risk by enrolment channel | Correct subgroup denominator; no language implying admission-time predictive accuracy | Planned |
| T-06 | R-06 | Attempt to see an individual student's record without permission | Sensitive data blocked; small groups suppressed according to agreed policy | Planned |
| T-07 | R-07 | Inject an invalid GPA, orphan key or impossible completion date in a test environment | Data validation fails and publishing is blocked | Planned |
| T-08 | R-08 | Show manager a high overdue metric | Manager can state the appropriate escalation and measure of effectiveness | Planned |

## Automated demonstration tests — completed

Running `python -m unittest discover -s demo/tests -v` invokes the deterministic generator and quality-audited SQLite analysis. Tests confirm row counts, key uniqueness, foreign-key coverage, range validity, consistent KPI bounds and seven zero-issue SQL checks.

**Test status applies only to the new synthetic demonstration.** It does not certify the original `.pbix` dashboard measures.

## Production reconciliation plan

1. Data owners approve all source columns, date fields and reporting populations.
2. BI analyst confirms counts before and after joins; prevents many-to-many multiplication.
3. Independent SQL calculations are compared with Power BI measures using the same filters.
4. Missing/invalid input tests are repeated on sample data with expected outputs.
5. Stakeholders check role-specific information access and decision usefulness.
6. Release is blocked if discrepancies remain; sign-off records business owner, version and data cut-off.

[Next → Implementation roadmap](08-implementation-roadmap.md)
