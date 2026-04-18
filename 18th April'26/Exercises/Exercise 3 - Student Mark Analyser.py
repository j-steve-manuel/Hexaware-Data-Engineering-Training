students = { "Rahul":85,
"Sneha":92,
"Arjun":78,
"Priya":88
}

# Tasks
# . Print the topper
for student in students.items():
    if(student[1] == max(students.values())):
        print(student[0])

# . Print average marks
print(sum(students.values())/len(students.values()))

# . Print students scoring above 85
for student in students.items():
    if(student[1] > 85):
        print(student[0])
