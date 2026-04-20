# Part 5 — Customer Analysis
import json
import csv

with open("products.json", "r") as file:
    content = json.load(file)
    data = content["products"]
    product = {i["product_id"]:{"name" : i["name"], "price": i["price"]} for i in data}
    print(product)

with open("orders.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    orders = {i["order_id"]: {"product_id": i["product_id"], "customer": i["customer"], "quantity":i["quantity"]} for i in csvreader }
    print(orders)

# Task 20
# Calculate total spending per customer.
spendings = {}
for i in orders.values():
    if(i["customer"] not in spendings.keys()):
        spendings[i["customer"]] = int(i["quantity"]) * product[int(i["product_id"])]["price"]
    else:
        spendings[i["customer"]] += int(i["quantity"]) * product[int(i["product_id"])]["price"]
print(spendings)

# Task 21
# Find the highest spending customer.
spender = ""
max_spendings = 0
for i in spendings:
    if(spendings[i] > max_spendings):
        max_spendings = spendings[i]
        spender = i
print("Highest spending Customer:", spender)

# Task 22
# Find customers who spent more than ₹50,000
customers = []
for i in spendings:
    if(spendings[i] > 50000):
        customers.append(i)
print(customers)



