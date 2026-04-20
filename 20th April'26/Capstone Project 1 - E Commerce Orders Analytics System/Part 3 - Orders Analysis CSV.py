# Part 3 — Orders Analysis (CSV)
import csv

# Task 12
# Read orders.csv .
with open("orders.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    print(csvreader)

# Task 13
# Print each order.
    for i in csvreader:
        print(i)

# Task 14
# Calculate the total quantity sold per product.
with open("orders.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    total_quantity = 0

    for i in csvreader:
        total_quantity += int(i["quantity"])

    print("Total products: ",total_quantity)

# Task 15
# Calculate total orders per customer.
# Expected structure:
# {
# "Rahul":3,
# "Sneha":2,
# "Arjun":1,
# "Priya":1,
# "Karan":1
# }
orders_customer = {}

with open("orders.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    for i in csvreader:
        if(i["customer"] not in orders_customer):
            orders_customer[i["customer"]] = 1
        else:
            orders_customer[i["customer"]] += 1
    print("Customer orders: ",orders_customer)

