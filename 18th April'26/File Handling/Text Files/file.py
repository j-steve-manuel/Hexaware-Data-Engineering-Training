# FILE HANDLING

# Reading file contents using for loop
with open("text.txt", "r") as file:
    for line in file:
        print(line.strip())

# Using readlines to read
with open("text.txt", "r") as file:
    content  = file.readlines()

print("Total students: ",len(content))


# Sum of values in a file
total = 0

with open("test2.txt", "r") as file:
    for line in file:
        total += int(line.strip())

print("Total sum: ",total)

# Writing contents to file
with open("text.txt", "w") as file:
    file.write("Rahul\n")
    file.write("Peter\n")
    file.write("Simon\n")

# Appending contents to file
print("After appending")
with open("text.txt", "a") as file:
    file.write("Steve\n")


values = ["Python\n", "Java\n", "Php\n"]
with open("languages.txt", "w") as file:
    file.writelines(values)
with open("languages.txt", "r") as file:
    content  = file.readlines()
for i in content:
    print(i)


