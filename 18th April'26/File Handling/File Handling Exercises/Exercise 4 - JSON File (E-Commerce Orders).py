import json
# File: orders.json
# {
# "orders": [
# {"order_id": 1, "customer": "Rahul", "amount": 2500},
# {"order_id": 2, "customer": "Sneha", "amount": 1800},
# {"order_id": 3, "customer": "Rahul", "amount": 3200},
# {"order_id": 4, "customer": "Arjun", "amount": 1500},
# {"order_id": 5, "customer": "Sneha", "amount": 2100}
# ]
# }
# Questions
with open("orders.json", "r") as orders:
    data = json.load(orders)
    data = data["orders"]

# 1. Print all orders.
for i in data:
    print(i)

# 2. Calculate total revenue.
total_revenue = 0
for i in data:
    total_revenue += i["amount"]
print(total_revenue)

# 3. Find total spending per customer.
spendings = {}
for i in data:
    if i["customer"] in spendings.keys():
        spendings[i["customer"]] += i["amount"]
    else:
        spendings[i["customer"]] = i["amount"]
print(spendings)

# 4. Find the highest spending customer.
max_spend = 0
spender = ""
for i in spendings:
    if(spendings[i] > max_spend):
        max_spend = spendings[i]
        spender = i
print(spender)

# 5. Count total orders per customer.
total_orders = {}
for i in data:
    if i["customer"] in total_orders.keys():
        total_orders[i["customer"]] += 1
    else:
        total_orders[i["customer"]] = 1
print(total_orders)
