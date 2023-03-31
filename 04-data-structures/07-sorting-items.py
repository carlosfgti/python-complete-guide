numbers = [89, 21, 2, 0, 34, 88123]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

numbers_sorted = sorted(numbers) # return new list
print(numbers_sorted)
numbers_sorted = sorted(numbers, reverse=True) # return new list
print(numbers_sorted)

print("-----------------")
cart = [
    ("Prod 1", 12.2),
    ("Prod 2", 13.2),
    ("Prod 0", 14.2),
]
def sort_cart(product):
    return product[1]

# sort cart by price
cart.sort(key=sort_cart)
print(cart)