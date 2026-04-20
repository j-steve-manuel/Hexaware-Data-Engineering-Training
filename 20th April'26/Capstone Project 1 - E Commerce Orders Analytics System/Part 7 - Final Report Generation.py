import json
import csv

# Part 7 — Data Structures
# Use:
# list → store orders
# dictionary → store product prices
# set → store unique visitors
# tuple → represent (product_name, revenue) pairs


# Part 8 — Final Report Generation
# Create a file called sales_report.txt.
# Example output:
# E-Commerce Sales Report
# Total Website Visits: 10
# Unique Visitors: 5
# Total Revenue: 181000
# Top Customer: Rahul
# Product Sales
# Laptop → 150000
# Mouse → 2500
# Keyboard → 4500
# Monitor → 24000


with open("products.json", "r") as file:
    content = json.load(file)
    data = content["products"]
    product = {i["product_id"]:{"name" : i["name"], "price": i["price"]} for i in data}
    print(product)

with open("orders.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    orders = {i["order_id"]: {"product_id": i["product_id"], "customer": i["customer"], "quantity":i["quantity"]} for i in csvreader }
    print(orders)

with open("website_visits.txt", "r") as file:
    file_content = file.read().split("\n")
    visitors = set(file_content)
    print(visitors)

# Final Challenge
# Task 29
# Find visitors who visited but never ordered anything.

ordered_customers = []
for i in orders.values():
    if(i["customer"] in ordered_customers):
        continue
    else:
        ordered_customers.append(i["customer"])

for i in visitors:
    if i not in ordered_customers:
        print(i," is only a visitor.")

# Task 30
# Find customers who ordered but never visited the website more than once.
visited_times = {}

for i in file_content:
    if i in visited_times:
        visited_times[i] += 1
    else:
        visited_times[i] = 1
for i in visited_times:
    if(visited_times[i] == 1):
        print(i," has purchased only once.")
