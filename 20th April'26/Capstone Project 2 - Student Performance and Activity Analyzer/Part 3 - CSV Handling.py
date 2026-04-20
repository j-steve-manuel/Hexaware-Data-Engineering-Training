# Part 3 — CSV Handling
import csv
# Task 13
# Read attendance.csv .
with open("attendance.csv") as attendance:
    reader = csv.reader(attendance)
    for row in reader:
        print(row)

# Task 14
# Print each student’s attendance details.
with open("attendance.csv") as attendance:
    reader = csv.DictReader(attendance)
    for row in reader:
        print(row)

# Task 15
# Calculate attendance percentage for each student.
print("Attendance Percentage ")
with open("attendance.csv") as attendance:
    reader = csv.DictReader(attendance)
    for row in reader:
        print(row["name"],":",(int(row["days_present"])/int(row["total_days"])*100) )
# Formula:
# (days_present / total_days) * 100

# Task 16
# Print students whose attendance is below 80%.
attendance_percent = {}
with open("attendance.csv") as attendance:
    reader = csv.DictReader(attendance)
    for row in reader:
        name = row["name"]
        attendance_percent["name"] = (int(row["days_present"])/int(row["total_days"])*100)
        if(attendance_percent["name"] < 80.0):
            print(name," has only ",attendance_percent["name"],"% attendance")

# Task 17
# Find the student with the best attendance.
attendance_percent = {}
max_percent = 0
regular = ""
with open("attendance.csv") as attendance:
    reader = csv.DictReader(attendance)
    for row in reader:
        name = row["name"]
        attendance_percent[name] = (int(row["days_present"])/int(row["total_days"])*100)
        if(attendance_percent[name] > max_percent):
            regular = row["name"]
            max_percent = attendance_percent[name]
    print(regular," has the best of ",max_percent,"% attendance")