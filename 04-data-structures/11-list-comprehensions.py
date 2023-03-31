cart = [
    ("Prod 1", 12.2),
    ("Prod 2", 13.2),
    ("Prod 0", 14.2),
]

# same result
prices = list(map(lambda product: product[1], cart))
print(prices)
prices = [product[1] for product in cart]
print(prices)

# same result
result = list(filter(lambda product: product[1] <= 14, cart))
print(result)
result = [product for product in cart if product[1] <= 14]
print(result)