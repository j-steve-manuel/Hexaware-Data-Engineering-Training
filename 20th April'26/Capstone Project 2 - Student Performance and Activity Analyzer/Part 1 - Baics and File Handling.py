# Part 1 — Basics and File Handling

# Task 1
# Read students.txt and print all names.
with open("students.txt", "r") as file:
    file = file.read().split()
    for line in file:
        print(line)

# Task 2
# Count the total number of entries in students.txt
print("Total numer of entries: ",len(file))

# Task 3
# Find the unique student names using a set.
print(set(file))

# Task 4
# Count how many times each student name appears using a dictionary.
name_count = {}
for name in file:
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1
for i in name_count:
    print(i,":",name_count[i])

# Task 5
# Write the unique student names into a new file called unique_students.txt .
print("Unique Students")
with open("unique_students.txt", "w") as file:
    file.writelines(name_count.keys())

with open("unique_students.txt", "r") as file:
    for line in file.readlines():
        print(line)

