inventory = { "laptop":10,
"mouse":25,
"keyboard":15
}

# Tasks
# . Add "monitor":8
inventory["monitor"] = 8
print(inventory)

# . Reduce laptop stock by 2
inventory["laptop"] -= 2
print(inventory)

# . Print items with stock less than 10
for i in inventory.items():
    if(i[1]<10):
        print(i[0])
