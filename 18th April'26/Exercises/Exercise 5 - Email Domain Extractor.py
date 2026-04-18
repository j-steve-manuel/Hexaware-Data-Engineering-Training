emails = [ "user1@gmail.com",
"user2@yahoo.com",
"user3@gmail.com",
"user4@outlook.com"
]

# Tasks
# . Extract domains

for email in emails:
    domain = email.split(".")
    print(domain[0])

# Count how many users per domain
# Expected output
# {
# "gmail.com":2,
# "yahoo.com":1, "outlook.com":1

domain_count = {}
for email in emails:
    domain = email.split("@")[1]
    if(domain in domain_count.keys()):
        domain_count[domain] += 1
    else:
        domain_count[domain] = 1

print(domain_count)

