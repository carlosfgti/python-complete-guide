numbers = [1, 2, 3]
first, second, third = numbers
print(first, second, third)
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

numbers2 = range(10)
first, second, *others, last = numbers2
print(first, second, last, others)