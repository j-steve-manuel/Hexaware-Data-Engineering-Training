orders = [
{"order_id":1,"customer":"Rahul","amount":2500},
{"order_id":2,"customer":"Sneha","amount":1800},
{"order_id":3,"customer":"Rahul","amount":3200},
{"order_id":4,"customer":"Amit","amount":1500}
]

# Tasks
# . Calculate total spending per customer
spendings = {}
for order in orders:
    if(order["customer"] not in spendings.keys()):
        spendings[order["customer"]] = order["amount"]
    else:
        spendings[order["customer"]] += order["amount"]
print(spendings)

# . Find highest spending customer
max_value = max(spendings.values())
for customer in spendings.keys():
    if(spendings[customer] == max_value):
        print(customer)
        break

# . Count total orders per customer
total_orders = {}
for order in orders:
    if(order["customer"] not in total_orders.keys()):
        total_orders[order["customer"]] = 1
    else:
        total_orders[order["customer"]] += 1
print(total_orders)