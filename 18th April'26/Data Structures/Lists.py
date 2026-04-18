numbers = [10,12,14,16,70]

print(numbers)

fruits = ["apple", "banana", "mango", "cherry"]

# Indexing
print(fruits[0])
print(fruits[1])

# Negative Indexing
print(fruits[-1])
print(fruits[-2])

# Updation
numbers = [10,20,30]
numbers[1] = 100
print(numbers)

# Adding element at end
numbers.append(40)
print(numbers)

# Insert
numbers.insert(1,5)
print(numbers)

# Remove
numbers = [10,20,30,40]
numbers.remove(30)
print(numbers)

# Remove last element
numbers.pop()
print(len(numbers))
print(numbers)

# Membership
numbers = [10,20,30,40]
for number in numbers:
    print(number)

fruits = ["apple", "banana", "mango"]
if "banana" in fruits:
    print("Banana exists")

numbers = [10,20,30,40,50]
print(numbers[1:4])

numbers = [10,120,310,40]
print(numbers[::-1])
numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

print(max(numbers))
print(min(numbers))
print(sum(numbers))

