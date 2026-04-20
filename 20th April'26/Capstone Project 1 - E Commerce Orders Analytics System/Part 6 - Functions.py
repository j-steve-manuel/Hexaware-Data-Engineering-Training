import json
import csv

# Part 6 — Functions
with open("products.json", "r") as file:
    content = json.load(file)
    data = content["products"]
    product = {i["product_id"]:{"name" : i["name"], "price": i["price"]} for i in data}
    print(product)

with open("orders.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    orders = {i["order_id"]: {"product_id": i["product_id"], "customer": i["customer"], "quantity":i["quantity"]} for i in csvreader }
    print(orders)

# Create functions for:

# Task 23
# Load visits from TXT.
def load_visits():
    with open("website_visits.txt", "r") as file:
        file_content = file.read().split("\n")
        print(file_content)
load_visits()

# Task 24
# Load product catalog from JSON.
def load_product_catalogue():
    with open("products.json", "r") as file:
        content = json.load(file)
        print(content["products"])
load_product_catalogue()

# Task 25
# Load orders from CSV.
def load_orders():
    with open("orders.csv", "r") as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',')
        print(csvreader)
        for i in csvreader:
            print(i)
load_orders()

# Task 26
# Calculate product revenue.
def product_revenue(product_id):
    quantity = 0
    for i in orders.values():
        if int(i["product_id"]) == product_id:
            quantity += int(i["quantity"])
    print("Product Revenue: ",product[product_id]["price"] * quantity)
product_revenue(102)

# Task 27
# Calculate customer spending.
def customer_spending(customer):
    spent = 0
    for i in orders.values():
        if i["customer"] == customer:
            p_id = int(i["product_id"])
            quantity = int(i["quantity"])
            price = product[p_id]["price"]
            spent += quantity * price
    return spent
customer_spending("Sneha")

# Task 28
# Find top customer.
def top_customer(customers):
    max_spent = 0
    spender = ""
    spend = {}
    for i in customers:
        spend[i] = customer_spending(i)
    for i in spend.items():
        if i[1]>max_spent:
            max_spent = i[1]
            spender = i[0]
    print(spender, "has spent a maximum of", max_spent)
top_customer(["Sneha","Rahul"])