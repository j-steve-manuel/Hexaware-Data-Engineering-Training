import csv

# File: sales.csv
# product,quantity,price
# Laptop,5,75000
# Mouse,20,500
# Keyboard,15,1500
# Laptop,3,75000
# Mouse,10,500

# Questions
with open("sales.csv") as sales:
    reader = csv.DictReader(sales)

    data = []
    for row in reader:
        data.append(row)
    print(data)

# 1. Calculate total sales revenue.
    sales_revenue = 0
    for row in data:
        sales_revenue += (int(row["price"]) * int(row["quantity"]))
    print(sales_revenue)

# 2. Find total quantity sold per product.
    qty_dict = {}
    for row in data:
        if(row["product"] in qty_dict.keys()):
            qty_dict[row["product"]] += int(row["quantity"])
        else:
            qty_dict[row["product"]] = int(row["quantity"])
    print(qty_dict)

# 3. Find the product with highest sales.
    sales_dict = {}
    for row in data:
        if(row["product"] in sales_dict.keys()):
            sales_dict[row["product"]] += (int(row["quantity"]))
        else:
            sales_dict[row["product"]] = (int(row["quantity"]))
    sales_max = max(sales_dict.values())
    for i in sales_dict.items():
        if i[1] == sales_max:
            print(f"Highest sales: {i[0]} with {i[1]} units.")


# 4. Calculate total revenue per product.
    total_revenue = {}
    for row in data:
        if(row["product"] in total_revenue.keys()):
            total_revenue[row["product"]] += (int(row["price"]) * int(row["quantity"]))
        else:
            total_revenue[row["product"]] = (int(row["price"]) * int(row["quantity"]))
    print(total_revenue)

# 5. Print products with sales above 50,000.
    sales_data = {}
    for row in data:
        if(row["product"] in sales_data.keys()):
            sales_data[row["product"]] += (int(row["price"]) * int(row["quantity"]))
        else:
            sales_data[row["product"]] = (int(row["price"]) * int(row["quantity"]))
    for i in sales_data.items():
        if i[1] >= 50000:
            print(i[0],"has a sales of ",i[1])



# Bonus Challenge
# Using the sales.csv file:
# Write Python code to produce this output:
# Product Sales Summary
# Laptop → Qty: 8 Revenue: 600000
# Mouse → Qty: 30 Revenue: 15000
# Keyboard → Qty: 15 Revenue: 22500


# Assuming sales.csv looks like this:
# product,quantity,price
# Laptop,5,75000
# Mouse,20,500
# Laptop,3,75000...

    product_summary = {}

    for row in data:
        name = row["product"]
        qty = int(row["quantity"])
        price = int(row["price"])
        revenue = qty * price

        if name not in product_summary:
            product_summary[name] = {"qty": 0, "rev": 0}

        product_summary[name]["qty"] += qty
        product_summary[name]["rev"] += revenue


    print("Product Sales Summary")
    for product, data in product_summary.items():
        print(f"{product} → Qty: {data['qty']} Revenue: {data['rev']}")

