products = { "Laptop":75000,
"Mobile":30000,
"Tablet":25000
}

# Tasks
# . Increase all prices by 10%
# . Print updated prices

for product in products.keys():
    products[product] = int(products[product] * 1.10)
print(products)

