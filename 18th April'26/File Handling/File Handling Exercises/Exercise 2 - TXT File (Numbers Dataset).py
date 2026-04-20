# File: numbers.txt
#
# 45
# 67
# 23
# 89
# 12
# 90
# 56
# 34
# 78
# 21
#
# Questions
#
# 1. Read all numbers from the file.
with open("numbers.txt", "r") as file:
    content = file.readlines()
    for i in content:
        print(int(i.strip()))

# 2. Calculate the sum of all numbers.
ans = 0
with open("numbers.txt", "r") as file:
    for i in file:
        ans += int(i.strip())
print("Sum is ",ans)

# 3. Find the maximum number.
with open("numbers.txt", "r") as file:
    content = file.readlines()
    for i in range(len(content)):
        content[i] = int(content[i])
print(max(content))

# 4. Find the minimum number.
print(min(content))

# 5. Count how many numbers are greater than 50.
count = 0
for i in content:
    if(i>50):
        count+=1
print("Total count > 50 is: ", count)
