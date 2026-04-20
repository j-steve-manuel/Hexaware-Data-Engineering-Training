# Part 2 — JSON Handling
import json

# Task 6
# Read marks.json .
with open("marks.json", "r") as file:
    file = json.load(file)
    data = file["students"]
for i in data:
    print(i)

# Task 7
# Print all student names and marks.
for i in data:
    print(i["name"]," - scored", i["marks"])

# Task 8
# Find the student with the highest marks.
max_score = 0
topper = ""

for i in data:
    if(i["marks"] > max_score):
        max_score = i["marks"]
        topper = i["name"]
print("Topper is",topper, "-", max_score)

# Task 9
# Find the student with the lowest marks.

min_score = data[0]["marks"]
for i in data:
    if(i["marks"] < min_score):
        min_score = i["marks"]
        name = i["name"]
print("Least Scorer is",name, "-", min_score)

# Task 10
# Calculate the average marks.
count = 0
marks = 0
for i in data:
    marks += i["marks"]
    count+=1
print("Avg score: ",marks/count)

# Task 11
# Print only students enrolled in the Python course.
print("Python enrolled students")
for i in data:
    if(i["course"] == "Python"):
        print(i["name"])

# Task 12
# Count how many students are there in each course using a dictionary.

course_dic = {}
for i in data:
    if(i["course"] in course_dic):
        course_dic[i["course"]] += 1
    else:
        course_dic[i["course"]] = 1
for i in course_dic:
    print(i, "-", course_dic[i])