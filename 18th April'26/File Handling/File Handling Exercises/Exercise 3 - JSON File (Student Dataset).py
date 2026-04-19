import json

# File: students.json
#
# {
# "students": [
# {"name": "Rahul", "marks": 85, "course": "Python"},
# {"name": "Sneha", "marks": 92, "course": "Data Science"},
# {"name": "Arjun", "marks": 78, "course": "Python"},
# {"name": "Priya", "marks": 88, "course": "AI"},
# {"name": "Karan", "marks": 70, "course": "Python"}
# ]
# }

# Questions
#
# 1. Print all student names.
with open("Student.json") as file:
    content = json.load(file)
# 2. Print students enrolled in Python course.
# 3. Find the student with highest marks.
# 4. Calculate average marks.
# 5. Count how many students are enrolled in each course.



