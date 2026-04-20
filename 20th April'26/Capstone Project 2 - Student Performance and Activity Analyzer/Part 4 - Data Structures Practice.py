# Part 4 — Data Structures Practice
import json
import csv
# Task 18
# Store all marks in a list and print:
# highest marks
# lowest marks
# sum of marks

with open("marks.json", "r") as file:
    file = json.load(file)
    data = file["students"]

    max_score = 0
    min_score = data[0]["marks"]
    sum_score = 0

    for i in data:
        if i["marks"] > max_score:
            max_score = i["marks"]
        elif i["marks"] < min_score:
            min_score = i["marks"]
        sum_score += i["marks"]

    print(max_score)
    print(min_score)
    print(sum_score)


# Task 19
# Create a tuple of all courses and print it.
with open("marks.json", "r") as file:
    ans = []
    file = json.load(file)
    data = file["students"]

    for i in data:
        print(i)
        ans.append(i["course"])
print(tuple(ans))


# Task 20
# Create a set of all courses to show unique courses.
unique_set = set()
with open("marks.json", "r") as file:
    file = json.load(file)
    data = file["students"]
    for i in data:
        unique_set.add(i["course"])
print(unique_set)

# Task 21
# Create a dictionary where:
# key = student name
# value = marks
# Create dictionary using a dictionary comprehension
student_marks_dict = {student['name']: student['marks'] for student in data}
print(student_marks_dict)


# Task 22
# Create a second dictionary where:
# key = student name
# value = attendance percentage
attendance_list = []
with open('attendance.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row['days_present'] = int(row['days_present'])
        row['total_days'] = int(row['total_days'])
        attendance_list.append(row)

attendance_pct_dict = {
    record['name']: (record['days_present'] / record['total_days']) * 100
    for record in attendance_list
}
for name, pct in attendance_pct_dict.items():
    print(f"{name}: {pct:.1f}%")
