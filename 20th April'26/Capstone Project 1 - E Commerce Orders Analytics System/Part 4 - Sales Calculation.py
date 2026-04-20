# Using product prices and order quantities:
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


# Task 16
# Calculate revenue for each order.
for order in orders.items():
    order_id = order[0]
    product_id = order[1]["product_id"]
    quantity = order[1]["quantity"]
    price = product[int(product_id)]["price"]

    print("Order ID:", order_id, ": Rs.", int(price) * int(quantity))

# Task 17
# Calculate total revenue.
total_revenue = 0
for order in orders.items():
    order_id = order[0]
    product_id = order[1]["product_id"]
    quantity = order[1]["quantity"]
    price = product[int(product_id)]["price"]

    total_revenue += int(price) * int(quantity)
print("Total Revenue:", total_revenue)


print(orders)
print(product)
# Task 18
# Calculate total revenue per product.
# Example output structure:
# {
# "Laptop":150000, "Mouse":2500,
# "Keyboard":4500,
# "Monitor":24000
# }
rev_per_product = {}
quantity = 0
for product in product.items():
    product_id = product[0]
    name = product[1]["name"]
    price = product[1]["price"]

    for order in orders.values():
        if(order["product_id"] == str(product_id)):
            quantity += int(order["quantity"])
    rev_per_product[name] = int(price) * int(quantity)
    quantity = 0
print(rev_per_product)


# Task 19
# Find the highest selling product by revenue
max_price = 0
product_sold = ""

for i in rev_per_product.items():
    if(i[1] > max_price):
        max_price = i[1]
        product_sold = i[0]
print(product_sold)
