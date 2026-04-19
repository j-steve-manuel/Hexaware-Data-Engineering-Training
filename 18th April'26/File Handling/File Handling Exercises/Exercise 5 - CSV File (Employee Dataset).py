import csv

# File: employees.csv
#
# name,department,salary
# Rahul,IT,70000
# Sneha,HR,60000
# Arjun,IT,75000
# Priya,Finance,80000
# Karan,IT,72000
#
# Questions
#
# 1. Print all employee names.
with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# 2. Find employees working in IT department.
# 3. Calculate the average salary.
# 4. Find the highest salary employee.
# 5. Count how many employees belong to each department.