# SETS

numbers = {10,20,30,40}
print(numbers)

numbers = {10,20,30,20,30,40}
print(numbers)

# List to Set
num = [10,40,20,20,30,50]
unique_numbers = set(num)
print(unique_numbers)

# Add
numbers = {10,20,30,40}
numbers.add(50)
print(numbers)

# Update
numbers = {10,20}
numbers.update([30,40,50])
print(numbers)

# Union of Sets
set1 = {10,20,30}
set2 = {20,30,40}

result = set1.union(set2)
print(result)

result = set1.difference(set2)
print(result)

result = set1.intersection(set2)
print(result)