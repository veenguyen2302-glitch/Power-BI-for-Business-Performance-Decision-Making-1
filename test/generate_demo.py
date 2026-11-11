"""Generate a privacy-safe synthetic demonstration dataset for Aurora University.
These rows are NEW portfolio examples, not recovered original academic data.
Python 3.9+; standard library only. Deterministic with seed 2026.
"""
from __future__ import annotations
import csv
import random
from pathlib import Path
from datetime import date, timedelta

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
SEED = 2026


def write_csv(path, fields, rows):
    with path.open('w', newline='', encoding='utf-8') as fp:
        writer = csv.DictWriter(fp, fieldnames=fields)
        writer.writeheader(); writer.writerows(rows)


def generate():
    DATA.mkdir(parents=True, exist_ok=True)
    rng = random.Random(SEED)
    courses = ['Business Law','Economics','Accounting','Statistics','Marketing',
               'Programming','Finance','Engineering','Mathematics']
    channels = ['Online Portal','Agent','University Fair','Referral']
    scholarship = ['None','Partial','Full']
    levels = ['Basic','Intermediate','Advanced']
    students, results = [], []
    for n in range(1,651):
        sid=f'AU-ST{n:04d}'
        entry=round(max(55,min(98,rng.gauss(77,9))),1)
        schol=rng.choices(scholarship, weights=[0.7,0.24,0.06])[0]
        english=rng.choices(levels,weights=[0.17,0.58,0.25])[0]
        channel=rng.choice(channels)
        course=rng.choice(courses)
        students.append(dict(student_id=sid,course_name=course,admission_channel=channel,
                             admission_score=entry,scholarship_type=schol,english_level=english,
                             enrolled_term='2026-T1'))
        study=max(1,min(35,round(rng.gauss(14.7,5.3),1)))
        attendance=max(32,min(100,round(rng.gauss(78,12),1)))
        # Intentional descriptive relationship; not a causal simulation or real outcome model.
        model=3.02+0.035*(study-15)+0.012*(attendance-78)+0.010*(entry-78)
        if schol != 'None': model += 0.08
        gpa=round(max(0,min(4,model+rng.gauss(0,0.54))),2)
        grade='HD' if gpa>=3.5 else 'D' if gpa>=3 else 'C' if gpa>=2.4 else 'P' if gpa>=2 else 'F'
        results.append(dict(result_id=f'AU-R{n:04d}',student_id=sid,course_name=course,
                            term='2026-T1',study_hours_week=study,
                            attendance_pct=attendance,gpa=gpa,grade=grade))
    write_csv(DATA/'students.csv',list(students[0]),students)
    write_csv(DATA/'student_results.csv',list(results[0]),results)
    with (DATA/'departments.csv').open(newline='',encoding='utf-8') as fp:
        departments=list(csv.DictReader(fp))
    campuses=['Main','City','North','West']
    systems=['HVAC','Electrical','Plumbing','Equipment','General']
    types=['Preventive','Reactive','Emergency']
    orders=[]
    for n in range(1,781):
        work=rng.choices(types,weights=[0.45,0.43,0.12])[0]
        prio=rng.choices([1,2,3,4,5],weights=([8,21,42,24,5] if work=='Preventive' else
                [3,15,38,34,10] if work=='Reactive' else [0,1,8,32,59]))[0]
        start=date(2026,1,1)+timedelta(days=rng.randint(0,222))
        duration=rng.randint(3,18) if work=='Preventive' else rng.randint(4,25) if work=='Reactive' else rng.randint(1,11)
        target=start+timedelta(days=duration)
        complete=rng.random() < (0.9 if work=='Preventive' else 0.77 if work=='Reactive' else 0.86)
        closed=max(start,target+timedelta(days=rng.choices([-7,-3,-1,0,1,3,7],weights=[17,20,24,18,10,8,3])[0])) if complete else None
        # Keep the snapshot date consistent with recorded completion evidence.
        if closed and closed > date(2026,9,1): closed = None
        done=closed is not None
        status='Completed' if done else 'Open'
        cost=round(max(120,rng.gauss(640,290))*(1.8 if work=='Emergency' else 1.1),2)
        satisfaction=(str(rng.randint(1,5)) if done and rng.random() < 0.78 else '')
        orders.append(dict(order_id=f'AU-W{n:04d}',department_id=rng.choice(departments)['department_id'],
                           campus=rng.choice(campuses),system_code=rng.choice(systems),work_type=work,
                           priority=prio,start_date=start.isoformat(),target_date=target.isoformat(),
                           completed_date=closed.isoformat() if done else '',status=status,
                           total_cost=cost,satisfaction_score=satisfaction))
    write_csv(DATA/'work_orders.csv',list(orders[0]),orders)
    print('Generated illustrative data:',len(students),'students,',len(results),'term results,',len(orders),'work orders')

if __name__ == '__main__':
    generate()
