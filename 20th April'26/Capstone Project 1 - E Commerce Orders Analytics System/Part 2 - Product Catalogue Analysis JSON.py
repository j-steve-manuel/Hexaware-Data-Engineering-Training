# Part 2 — Product Catalog Analysis (JSON)
import json

# Task 7
# Read products.json .
with open("products.json", "r") as file:
    content = json.load(file)
    data = content["products"]
print(data)

# Task 8
# Print all product names and prices.
for i in data:
    print(i["name"],"- Rs.", i["price"])

# Task 9
# Store product information in a dictionary.
# Example structure:
# {
# 101: {"name":"Laptop","price":75000},
# 102: {"name":"Mouse","price":500}
# }
product_info = {}

for i in data:
    product_info[i["product_id"]] = {"name": i["name"], "price": i["price"]}
print(product_info)

# Task 10
# Find the most expensive product.
product = ""
max_price =0

for i in product_info.values():
    if(i["price"] > max_price):
        max_price = i["price"]
        product = i["name"]
print("Maximum priced product: ", product, ": Rs.", max_price)

# Task 11
# Find the least expensive product.
product = ""
min_price = max_price

for i in product_info.values():
    if(i["price"] < min_price):
        min_price = i["price"]
        product = i["name"]
print("Minimum priced product: ", product, ": Rs.", min_price)

