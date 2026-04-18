sales = [ {"product":"Laptop","qty":5},
{"product":"Mouse","qty":20},
{"product":"Laptop","qty":3},
{"product":"Keyboard","qty":10}
]

# Tasks
# . Calculate total sales per product
# . Find highest selling product

quantities = []

for sample in sales:
    quantities.append(sample["qty"])

maximum_qty = max(quantities)

for i in sales:
    if(i["qty"] == maximum_qty):
        print(i["product"]+" is the highest selling product.")
