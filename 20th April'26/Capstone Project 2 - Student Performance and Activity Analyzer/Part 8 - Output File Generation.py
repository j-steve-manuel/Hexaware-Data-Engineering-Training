# Part 8 — Output File Generation
import json
import csv

with open('marks.json', 'r') as f:
    marks_json = json.load(f)['students']

attendance_lookup = {}
with open('attendance.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        pct = (int(row['days_present']) / int(row['total_days'])) * 100
        attendance_lookup[row['name']] = pct

final_data = {}
for student in marks_json:
    name = student['name']
    final_data[name] = {
        "marks": student['marks'],
        "attendance": attendance_lookup.get(name, 0), # Get pct, default to 0 if name missing
        "course": student['course']
    }

# Task 37
# Write the final student summary to a text file called report.txt .
# {
# "Rahul": {"marks": 85, "attendance": 88.0, "course": "Python"},
# "Sneha": {"marks": 92, "attendance": 96.0, "course": "Data Engineering"
# }
# Expected style:
# Student Report
# Rahul - Marks: 85 - Attendance: 88.0% - Grade: B
# Sneha - Marks: 92 - Attendance: 96.0% - Grade: A
# Arjun - Marks: 78 - Attendance: 80.0% - Grade: B
def get_grade(mark):
    if mark >= 90:
        return 'A'
    elif mark >= 75:
        return 'B'
    elif mark >= 50:
        return 'C'
    else:
        return 'Fail'

with open('report.txt', 'w') as f:
    for name, info in final_data.items():
        grade = get_grade(info['marks'])
        line = f"{name} - Marks: {info['marks']} - Attendance: {info['attendance']:.1f}% - Grade: {grade}\n"
        f.write(line)

# Task 38
# Write only eligible students to eligible_students.txt .
MIN_MARKS = 75
MIN_ATTENDANCE = 80

with open('eligible_students.txt', 'w') as f:
    for name, info in final_data.items():
        if info['marks'] >= MIN_MARKS and info['attendance'] >= MIN_ATTENDANCE:
            f.write(f"{name}\n")