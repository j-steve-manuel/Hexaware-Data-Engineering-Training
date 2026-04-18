logins = [ ("Rahul","10:00"),
("Sneha","10:10"),
("Rahul","11:00"),
("Arjun","11:15"),
("Sneha","11:30")
]
# Tasks
# . Count how many times each user logged in
# . Store results in dictionary
# Expected output
# {
# "Rahul":2,
# "Sneha":2,
# "Arjun":1
# }

users = {}
for i in logins:
    if(i[0] not in users.keys()):
        users[i[0]] = 1
    else:
        users[i[0]] += 1
print(users)