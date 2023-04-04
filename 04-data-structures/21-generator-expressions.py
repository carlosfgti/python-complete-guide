from sys import getsizeof

values = (x * 2 for x in range(40000))
print(values) # generator
print("gen: ", getsizeof(values))

values = [x * 2 for x in range(40000)]
print(values) # list
print("list: ", getsizeof(values))
# for value in values:
#     print(value)
