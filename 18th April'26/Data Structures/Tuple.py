 # Tuple  - latitudes and longitudes (coordinates), config values
numbers = (10,20,30,40)
print(numbers)


fruits = ("Apple", "banana", "mango")

# Indexing
print(fruits[0])
print(fruits[1])

# Negative Indexing
print(fruits[-1])
print(fruits[-2])

# Length of a tuple
print(len(fruits))

numbers = (10, 20, 30, 40)
for i in numbers:
    print(i)

# this cant be done as tuples are immutable
numbers = (10,20,30,40)
# numbers[0] = 100


# Packing and Unpacking

# Packing
student = ("John", 20, 100)
print(student)

# Unpacking
name, age, marks = student
print(name)
print(age)
print(marks)

# Multi type values
data = ("Steve", 25, True, 120000,00)
print(data)
print(type(data))
