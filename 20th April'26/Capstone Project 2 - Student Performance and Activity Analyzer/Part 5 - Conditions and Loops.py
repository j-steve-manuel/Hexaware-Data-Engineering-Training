import json
import csv

# Part 5 — Conditions and Loops

try:
    with open('marks.json', 'r') as f:
        data = json.load(f)
        marks_data = data['students']
        student_marks_dict = {s['name']: s['marks'] for s in marks_data}
except FileNotFoundError:
    print("Error: marks.json not found.")
    student_marks_dict = {}

attendance_pct_dict = {}
try:
    with open('attendance.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['name']
            present = int(row['days_present'])
            total = int(row['total_days'])
            attendance_pct_dict[name] = (present / total) * 100
except FileNotFoundError:
    print("Error: attendance.csv not found.")


# Task 23
# Using a loop, print whether each student is:
# "Pass" if marks >= 50
# "Fail" otherwise
for name, marks in student_marks_dict.items():
    status = "Pass" if marks >= 50 else "Fail"
    print(f"{name}: {status}")


# Task 24
# Using conditions, assign grades:
# 90 and above → A
# 75 to 89 → B
# 50 to 74 → C
# below 50 → Fail
print("--- Task 24: Grades ---")
for name, marks in student_marks_dict.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"
    print(f"{name}: {grade}")

# Task 25
# Print all students who have:
# marks above 80
# attendance above 85%
for name, marks in student_marks_dict.items():
    # We use .get() to avoid errors if a name is missing in attendance
    attendance = attendance_pct_dict.get(name, 0)

    if marks > 80 and attendance > 85:
        print(f"Top Performer: {name} (Marks: {marks}, Attendance: {attendance:.1f}%)")
