# Given a list of numbers:
numbers = [10,20,10,30,20,10,40]

# Tasks
# . Count how many times each number appears
# . Store the result in a dictionary

# Expected structure
# {10:3, 20:2, 30:1, 40:1}

ans = {}
for i in numbers:
    if i in ans:
        ans[i] += 1
    else:
        ans[i] = 1

print(ans)