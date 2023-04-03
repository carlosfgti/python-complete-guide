numbers = [1, 2, 2, 2, 3, 4]
print(numbers)
uniques = set(numbers)
print(uniques)

print("----------")
first = set([1, 2, 3, 4])
second = {1, 5}
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)