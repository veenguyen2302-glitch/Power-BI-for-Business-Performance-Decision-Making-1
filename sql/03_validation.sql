-- Return 0 for all issue_count metrics in a clean synthetic demonstration.
SELECT 'missing_students' AS check_name, COUNT(*) AS issue_count
FROM student_results r LEFT JOIN students s ON r.student_id=s.student_id WHERE s.student_id IS NULL
UNION ALL SELECT 'missing_departments',COUNT(*)
FROM work_orders w LEFT JOIN departments d ON w.department_id=d.department_id WHERE d.department_id IS NULL
UNION ALL SELECT 'gpa_outside_0_4',COUNT(*) FROM student_results WHERE gpa<0 OR gpa>4
UNION ALL SELECT 'attendance_outside_0_100',COUNT(*) FROM student_results WHERE attendance_pct<0 OR attendance_pct>100
UNION ALL SELECT 'priority_outside_1_5',COUNT(*) FROM work_orders WHERE priority<1 OR priority>5
UNION ALL SELECT 'invalid_satisfaction',COUNT(*) FROM work_orders WHERE satisfaction_score NOT BETWEEN 1 AND 5 AND satisfaction_score IS NOT NULL
UNION ALL SELECT 'invalid_dates',COUNT(*) FROM work_orders WHERE completed_date<start_date AND completed_date IS NOT NULL;
