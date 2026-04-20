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
with open("students.json", "r") as file:
    content = json.load(file)
    data = content["students"]

# 1. Print all student names.
    for i in data:
        print(i["name"])

# 2. Print students enrolled in Python course.
    for i in data:
        if i["course"] == "Python":
            print(i["name"])

# 3. Find the student with highest marks.
    MAX_MARKS = 0
    topper = ""
    for i in data:
        if(i["marks"]>MAX_MARKS):
            topper = i["name"]
            MAX_MARKS = i["marks"]
    print(topper, "scored", MAX_MARKS)

# 4. Calculate average marks.
    avg_marks = 0
    for i in data:
        avg_marks += i["marks"]
    print("Average marks: ", avg_marks/(len(data)))

# 5. Count how many students are enrolled in each course.
    courses = {}
    for i in data:
        if i["course"] in courses.keys():
            courses[i["course"]] += 1
        else:
            courses[i["course"]] = 1

    for i in courses.items():
        print(i)


