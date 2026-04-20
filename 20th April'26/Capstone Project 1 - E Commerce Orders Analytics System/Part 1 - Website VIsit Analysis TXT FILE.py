# Part 1 — Website Visit Analysis (TXT)

# Task 1
# Read website_visits.txt .
with open("website_visits.txt", "r") as file:
    file_content = file.read().split("\n")
    print(file_content)

# Task 2
# Print all visitors.
for i in file_content:
    print(i)

# Task 3
# Find the total number of visits.
print("Total visits:",len(file_content))

# Task 4
# Find unique visitors using a set.
print("Unique visitors are: ",set(file_content))

# Task 5
# Count how many times each visitor came to the website.
# Example expected structure:
# {
# "Rahul":3,
# "Sneha":3,
# "Arjun":2,
# "Priya":1,
# "Karan":1
total_visits = {}

for i in file_content:
    if i in total_visits.keys():
        total_visits[i] += 1
    else:
        total_visits[i] = 1
print(total_visits)

# Task 6
# Find the most frequent visitor.
max_visits = 0
freq_visitor = []
for i in total_visits.keys():
    if(total_visits[i] > max_visits):
        freq_visitor = [i]
        max_visits = total_visits[i]
    elif(total_visits[i] == max_visits):
        freq_visitor.append(i)
    else:
        continue
print("Frequent visitors are: ")
for i in freq_visitor:
    print(i)

