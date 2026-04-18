# Dictionary
student = {
    "name" : "Steve",
    "age" : 25,
    "score" : 100
}

print(student)
print(student["name"])
print(student["age"])
print(student["score"])

#  GET
print(student.get("name"))
print(student.get("age"))

# Update values
student["age"] = 22
print(student)

# Add a new pair
student["city"]  = "New York"
print(student)

# Built in functions
print(student.keys())
print(student.values())
print(student.items())

