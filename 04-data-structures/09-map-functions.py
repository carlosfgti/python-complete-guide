cart = [
    ("Prod 1", 12.2),
    ("Prod 2", 13.2),
    ("Prod 0", 14.2),
]

prices = []
for product in cart:
    prices.append(product[1])
print(prices)

prices2 = map(lambda product: product[1], cart)
for price in prices2:
    print(price)

prices3 = list(map(lambda product: product[1], cart))
print(prices3)