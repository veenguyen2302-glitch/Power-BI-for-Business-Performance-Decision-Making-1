-- Queries use SQLite syntax; execute after loading via demo/scripts/analyse.py.
-- (1) Faculty: student outcomes, no SUM(GPA) or assumed causal relationships.
SELECT course_name, COUNT(*) AS results,
 ROUND(AVG(gpa),2) AS avg_gpa,
 ROUND(AVG(attendance_pct),1) AS avg_attendance_pct,
 ROUND(100.0*AVG(CASE WHEN grade <> 'F' THEN 1.0 ELSE 0.0 END),1) AS pass_rate_pct
FROM student_results GROUP BY course_name ORDER BY avg_gpa;
-- (2) Facilities: overdue rate and spending by *work order*.
SELECT work_type, COUNT(*) AS work_orders,
 ROUND(AVG(priority),2) AS mean_priority,
 ROUND(SUM(total_cost),2) AS total_cost,
 ROUND(100.0*AVG(CASE WHEN status='Completed' THEN 1.0 ELSE 0.0 END),1) AS completion_rate_pct,
 ROUND(100.0*AVG(CASE WHEN (status='Completed' AND completed_date>target_date)
  OR (status='Open' AND target_date<'2026-09-01') THEN 1.0 ELSE 0.0 END),1) AS overdue_rate_pct
FROM work_orders GROUP BY work_type ORDER BY overdue_rate_pct DESC;
-- (3) Admissions: descriptive *post-term* at-risk status, not predictive admissions risk.
SELECT s.admission_channel, COUNT(DISTINCT s.student_id) AS students,
 ROUND(AVG(r.gpa),2) AS mean_current_gpa,
 ROUND(100.0*AVG(CASE WHEN r.gpa<2.0 OR r.attendance_pct<65 THEN 1.0 ELSE 0.0 END),1) AS observed_at_risk_pct
FROM students s JOIN student_results r ON r.student_id=s.student_id
GROUP BY s.admission_channel ORDER BY observed_at_risk_pct DESC;
