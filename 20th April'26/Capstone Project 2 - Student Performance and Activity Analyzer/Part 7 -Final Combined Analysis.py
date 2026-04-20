# Part 7 — Final Combined Analysis

import json
import csv

with open('marks.json', 'r') as f:
    marks_data = json.load(f)['students']

attendance_list = []
with open('attendance.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        attendance_list.append({
            "name": row['name'],
            "present": int(row['days_present']),
            "total": int(row['total_days'])
        })

# Task 33
# Combine marks and attendance data and create a final structure like this:
# {
# "Rahul": {"marks": 85, "attendance": 88.0, "course": "Python"},
# "Sneha": {"marks": 92, "attendance": 96.0, "course": "Data Engineering}
# }

final_data = {}

for item in marks_data:
    name = item['name']
    marks = item['marks']
    course = item['course']

    att_record = next(a for a in attendance_list if a['name'] == name)
    att_pct = (att_record['present'] / att_record['total']) * 100

    final_data[name] = {
        "marks": marks,
        "attendance": att_pct,
        "course": course
    }

# Task 34
# From this combined structure, print:
# name
# marks
# attendance
# course
# grade
def get_grade(mark):
    if mark >= 90:
        return 'A'
    elif mark >= 75:
        return 'B'
    elif mark >= 50:
        return 'C'
    else:
        return 'Fail'

for name, info in final_data.items():
    grade = get_grade(info['marks'])
    print(f"{name:<10} | {info['marks']:<5} | {info['attendance']:<8.1f} | {info['course']:<15} | {grade}")

# Task 35
# Find students who are eligible for certification.
# Condition:
# marks >= 75
# attendance >= 80

eligible_students = []
print("\nTask 35: Eligible for Certification")
for name, info in final_data.items():
    if info['marks'] >= 75 and info['attendance'] >= 80:
        eligible_students.append(name)
        print(f"- {name}")

# Task 36
# Find students who need improvement.
# Condition:
# marks < 75 or attendance < 80

improvement_needed = []
print("Improvement needed:")
for name, info in final_data.items():
    if info['marks'] < 75 or info['attendance'] < 80:
        improvement_needed.append(name)
        print(f"{name}")