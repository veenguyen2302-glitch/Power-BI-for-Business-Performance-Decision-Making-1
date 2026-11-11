-- Illustrative portfolio data model. These are NOT the original MIS781 source tables.
-- One row per enrolled student. NO personally identifying fields.
CREATE TABLE IF NOT EXISTS students (
 student_id TEXT PRIMARY KEY,
 course_name TEXT NOT NULL,
 admission_channel TEXT NOT NULL,
 admission_score REAL NOT NULL,
 scholarship_type TEXT NOT NULL,
 english_level TEXT NOT NULL,
 enrolled_term TEXT NOT NULL
);
-- One row per student x course x term in this synthetic demonstration.
CREATE TABLE IF NOT EXISTS student_results (
 result_id TEXT PRIMARY KEY,
 student_id TEXT NOT NULL REFERENCES students(student_id),
 course_name TEXT NOT NULL,
 term TEXT NOT NULL,
 study_hours_week REAL NOT NULL,
 attendance_pct REAL NOT NULL,
 gpa REAL NOT NULL,
 grade TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS departments (
 department_id TEXT PRIMARY KEY,
 department_name TEXT NOT NULL
);
-- Work orders are events, not department rows. Do not fan out totals via raw joins.
CREATE TABLE IF NOT EXISTS work_orders (
 order_id TEXT PRIMARY KEY,
 department_id TEXT NOT NULL REFERENCES departments(department_id),
 campus TEXT NOT NULL,
 system_code TEXT NOT NULL,
 work_type TEXT NOT NULL,
 priority INTEGER NOT NULL,
 start_date TEXT NOT NULL,
 target_date TEXT NOT NULL,
 completed_date TEXT,
 status TEXT NOT NULL,
 total_cost REAL NOT NULL,
 satisfaction_score INTEGER
);
CREATE INDEX IF NOT EXISTS idx_student_results_student ON student_results(student_id);
CREATE INDEX IF NOT EXISTS idx_work_orders_department ON work_orders(department_id);
