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
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    data = []
    for row in reader:
        data.append(row)
    print(data)

# 1. Print all employee names.
    for val in data:
        print(val["name"])

# 2. Find employees working in IT department.
    for row in data:
        if(row["department"] == "IT"):
            print(row["name"], ": IT")

# 3. Calculate the average salary.
    salary = []
    for row in data:
        salary.append(int(row["salary"]))
    print("The average salary :",sum(salary)/len(salary))

# 4. Find the highest salary employee.
    for row in data:
        if(int(row["salary"]) == max(salary)):
            print(row["name"], "is the highly paid employee.")

# 5. Count how many employees belong to each department.
    dept_count = {}
    for row in data:
        if row["department"] in dept_count.keys() :
            dept_count[row["department"]] += 1
        else:
            dept_count[row["department"]] = 1
    print(dept_count)

