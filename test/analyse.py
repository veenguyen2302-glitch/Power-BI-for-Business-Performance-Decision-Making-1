"""Validate and analyse the synthetic Aurora demonstration, then build its static site feed.
No external packages, no access to real student records, no network connections.
"""
from __future__ import annotations
import csv
import json
import sqlite3
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'; OUTPUT=ROOT/'outputs'; SQL=ROOT/'sql'; SITE=ROOT.parent/'site'


def load(conn, table, file, converters=None):
    converters=converters or {}
    with (DATA/file).open(newline='',encoding='utf-8') as fp:
        reader=csv.DictReader(fp)
        header=reader.fieldnames
        rows=[]
        for raw in reader:
            r=[]
            for field in header:
                val=raw.get(field,'')
                if val is None or val=='': val=None
                elif field in converters: val=converters[field](val)
                r.append(val)
            rows.append(r)
    placeholders=','.join(['?']*len(header))
    conn.executemany(f"INSERT INTO {table} ({','.join(header)}) VALUES ({placeholders})",rows)
    return len(rows)


def read_query(conn,q):
    cur=conn.execute(q)
    return [dict(zip([d[0] for d in cur.description],row)) for row in cur.fetchall()]


def save_csv(name,rows):
    if not rows: return
    with (OUTPUT/name).open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)


def bar_svg(title,subtitle,items,value_key,label_key,path,unit='',limit=8):
    items=items[:limit]
    values=[float(row[value_key]) for row in items]
    maxi=max(values,default=1)
    width=980; left=230; top=108; rowheight=53; right=120
    height=top+len(items)*rowheight+78
    bg='#ffffff'; navy='#163a56'; teal='#18a999'
    s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-label="{title}">',
       '<rect width="100%" height="100%" fill="#fff"/>',
       f'<text x="30" y="39" font-size="24" font-family="Arial" font-weight="bold" fill="{navy}">{title}</text>',
       f'<text x="30" y="66" font-size="14" font-family="Arial" fill="#657789">{subtitle}</text>']
    for i,row in enumerate(items):
        y=top+i*rowheight
        val=float(row[value_key]); label=str(row[label_key]); barmax=width-left-right
        s.append(f'<text x="30" y="{y+21}" font-size="16" font-family="Arial" fill="{navy}">{label}</text>')
        s.append(f'<rect x="{left}" y="{y}" width="{barmax}" height="27" rx="6" fill="#e9f1f4"/>')
        s.append(f'<rect x="{left}" y="{y}" width="{max(0,barmax*val/maxi):.0f}" height="27" rx="6" fill="{teal}"/>')
        s.append(f'<text x="{width-24}" y="{y+21}" text-anchor="end" font-family="Arial" font-weight="bold" font-size="16" fill="{navy}">{val:,.1f}{unit}</text>')
    s.append(f'<text x="30" y="{height-21}" font-size="13" font-family="Arial" fill="#657789">ILLUSTRATIVE SYNTHETIC DATA — generated for portfolio reproducibility, not the original Power BI results</text>')
    s.append('</svg>')
    path.write_text('\n'.join(s),encoding='utf-8')


def main():
    OUTPUT.mkdir(parents=True,exist_ok=True)
    SITE.mkdir(parents=True,exist_ok=True)
    conn=sqlite3.connect(':memory:'); conn.execute('PRAGMA foreign_keys=ON')
    conn.executescript((SQL/'01_schema.sql').read_text(encoding='utf-8'))
    counts={}
    counts['departments']=load(conn,'departments','departments.csv')
    counts['students']=load(conn,'students','students.csv',{'admission_score':float})
    counts['results']=load(conn,'student_results','student_results.csv',{'gpa':float,'study_hours_week':float,'attendance_pct':float})
    counts['work_orders']=load(conn,'work_orders','work_orders.csv',{'priority':int,'total_cost':float,'satisfaction_score':int})
    checks=read_query(conn,(SQL/'03_validation.sql').read_text(encoding='utf-8'))
    if any(r['issue_count']!=0 for r in checks):
        raise ValueError('Data-quality failure: '+repr(checks))
    faculty=read_query(conn,"""SELECT course_name,COUNT(*) AS records, ROUND(AVG(gpa),2) AS avg_gpa,
      ROUND(AVG(attendance_pct),1) AS avg_attendance_pct,
      ROUND(100.0*AVG(CASE WHEN grade<>'F' THEN 1.0 ELSE 0 END),1) AS pass_rate_pct
      FROM student_results GROUP BY course_name ORDER BY avg_gpa DESC""")
    facilities=read_query(conn,"""SELECT work_type,COUNT(*) AS orders,
      ROUND(AVG(priority),2) AS avg_priority,
      ROUND(SUM(total_cost),2) AS total_cost,
      ROUND(100.0*AVG(CASE WHEN status='Completed' THEN 1.0 ELSE 0.0 END),1) AS completion_pct,
      ROUND(100.0*AVG(CASE WHEN (status='Completed' AND completed_date>target_date)
       OR (status='Open' AND target_date<'2026-09-01') THEN 1.0 ELSE 0.0 END),1) AS overdue_pct
      FROM work_orders GROUP BY work_type ORDER BY overdue_pct DESC""")
    dept=read_query(conn,"""SELECT d.department_name,COUNT(*) AS orders,
      ROUND(AVG(w.total_cost),2) AS avg_cost,
      ROUND(SUM(w.total_cost),2) AS total_cost,
      ROUND(100.0*AVG(CASE WHEN (w.status='Completed' AND w.completed_date>w.target_date)
       OR (w.status='Open' AND w.target_date<'2026-09-01') THEN 1.0 ELSE 0.0 END),1) AS overdue_pct
      FROM work_orders w JOIN departments d ON w.department_id=d.department_id
      GROUP BY d.department_id HAVING COUNT(*)>=10 ORDER BY overdue_pct DESC LIMIT 10""")
    admissions=read_query(conn,"""SELECT s.admission_channel,COUNT(*) AS students,
      ROUND(AVG(r.gpa),2) AS mean_current_gpa,
      ROUND(100.0*AVG(CASE WHEN r.gpa<2.0 OR r.attendance_pct<65 THEN 1.0 ELSE 0.0 END),1) AS current_risk_pct
      FROM students s JOIN student_results r ON s.student_id=r.student_id
      GROUP BY s.admission_channel ORDER BY current_risk_pct DESC""")
    scholar=read_query(conn,"""SELECT s.scholarship_type,COUNT(*) AS students,
      ROUND(AVG(r.gpa),2) AS avg_gpa,ROUND(AVG(r.attendance_pct),1) AS avg_attendance_pct
      FROM students s JOIN student_results r ON s.student_id=r.student_id
      GROUP BY s.scholarship_type ORDER BY avg_gpa DESC""")
    overall=read_query(conn,"""SELECT ROUND(AVG(gpa),2) AS avg_gpa,
      ROUND(100.0*AVG(CASE WHEN grade<>'F' THEN 1.0 ELSE 0.0 END),1) AS pass_rate_pct
      FROM student_results""")[0]
    work=read_query(conn,"""SELECT COUNT(*) AS work_orders, ROUND(SUM(total_cost),2) AS work_order_cost,
       ROUND(100.0*AVG(CASE WHEN (status='Completed' AND completed_date>target_date)
       OR (status='Open' AND target_date<'2026-09-01') THEN 1.0 ELSE 0.0 END),1) AS overdue_pct FROM work_orders""")[0]
    high=read_query(conn,"""SELECT ROUND(100.0*AVG(CASE WHEN gpa<2.0 OR attendance_pct<65 THEN 1.0 ELSE 0.0 END),1) AS current_risk_pct FROM student_results""")[0]
    for fn,rows in [('faculty_by_course.csv',faculty),('facilities_by_type.csv',facilities),
                    ('facilities_top_departments.csv',dept),('admissions_by_channel.csv',admissions),
                    ('scholarship_associations.csv',scholar),('validation_results.csv',checks)]: save_csv(fn,rows)
    bar_svg('Average GPA by course','Mean within course; not SUM(GPA)',faculty,'avg_gpa','course_name',OUTPUT/'faculty_gpa.svg')
    bar_svg('Overdue work orders by type','Late completed or open past due at 2026-09-01',facilities,'overdue_pct','work_type',OUTPUT/'facilities_overdue.svg','%')
    bar_svg('Observed current-risk rate by entry channel','Descriptive, post-term flag; NOT admissions prediction',admissions,'current_risk_pct','admission_channel',OUTPUT/'admissions_risk.svg','%')
    payload={'notice':'DEMONSTRATION ONLY: newly generated synthetic data, not the original MIS781 Power BI data',
      'snapshot_date':'2026-09-01','counts':counts,
      'overall':{**overall,**work,**high},'faculty':faculty,'facilities':facilities,
      'facility_departments':dept,'admissions':admissions,'scholarship':scholar,'checks':checks}
    (OUTPUT/'portfolio_metrics.json').write_text(json.dumps(payload,indent=2),encoding='utf-8')
    (SITE/'data.js').write_text('window.AURORA_DEMO = '+json.dumps(payload,ensure_ascii=False)+';\n',encoding='utf-8')
    print('Validation passed:',len(checks),'checks |',counts,'|',payload['overall'])

if __name__=='__main__':
    main()
