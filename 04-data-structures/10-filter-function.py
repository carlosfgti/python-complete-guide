cart = [
    ("Prod 1", 12.2),
    ("Prod 2", 13.2),
    ("Prod 0", 14.2),
]

result = list(filter(lambda product: product[1] <= 14, cart))
print(result)