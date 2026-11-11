"""Baseline checks for the deterministic synthetic demonstration pipeline."""
import csv
import json
import subprocess
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def rows(name):
    with (ROOT/'data'/name).open(newline='',encoding='utf-8') as f:
        return list(csv.DictReader(f))

class DemoPipelineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run([sys.executable,str(ROOT/'scripts'/'generate_demo.py')],check=True)
        subprocess.run([sys.executable,str(ROOT/'scripts'/'analyse.py')],check=True)
    def test_row_counts(self):
        self.assertEqual(len(rows('students.csv')),650)
        self.assertEqual(len(rows('student_results.csv')),650)
        self.assertEqual(len(rows('work_orders.csv')),780)
    def test_integrity(self):
        students=rows('students.csv'); results=rows('student_results.csv'); orders=rows('work_orders.csv')
        ids={r['student_id'] for r in students}
        self.assertEqual(len(ids),len(students))
        self.assertTrue(all(r['student_id'] in ids for r in results))
        self.assertEqual(len({r['order_id'] for r in orders}),len(orders))
        self.assertTrue(all(0<=float(r['gpa'])<=4 and 0<=float(r['attendance_pct'])<=100 for r in results))
    def test_metrics_and_quality(self):
        p=json.loads((ROOT/'outputs'/'portfolio_metrics.json').read_text())
        self.assertTrue(all(v['issue_count']==0 for v in p['checks']))
        self.assertTrue(0<=p['overall']['pass_rate_pct']<=100)
        self.assertTrue(0<=p['overall']['overdue_pct']<=100)
        self.assertEqual(p['counts']['departments'],50)

if __name__=='__main__': unittest.main()
