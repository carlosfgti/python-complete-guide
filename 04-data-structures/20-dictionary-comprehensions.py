values = []
for x in range(10):
    values.append(x + 2)
print(values)

# values2 = [expression for x in range(10)]
values2 = [x + 2 for x in range(10)]
print(values2)

# ------------------------------------------
# dictionary
values3 = {x + 2 for x in range(10)}
print(values3)

values4 = {x: x + 2 for x in range(10)}
print(values4)