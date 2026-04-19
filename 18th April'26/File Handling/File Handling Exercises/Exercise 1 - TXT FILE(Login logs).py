# File: logins.txt
#
# Rahul
# Sneha
# Rahul
# Arjun
# Sneha
# Rahul
# Karan

# Questions
#
# 1. Read the file and print all names.
with open("logins.txt", "r") as file:
    login = file.readlines()
    for i in login:
        print(i)

# 2. Count the total number of login records.
print(len(login))

# 3. Find how many times each user logged in.
dict = {}

for i in login:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)

# 4. Find the user who logged in the most.


# 5. Print the unique users.
print(set(login))
