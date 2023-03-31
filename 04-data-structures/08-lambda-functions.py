cart = [
    ("Prod 1", 12.2),
    ("Prod 2", 13.2),
    ("Prod 0", 14.2),
]
def sort_cart(product):
    return product[1]

# sort cart by price
# cart.sort(key=sort_cart)
cart.sort(key=lambda product:product[1])
print(cart)