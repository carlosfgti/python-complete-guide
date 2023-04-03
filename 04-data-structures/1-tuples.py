point = 1, 2
print(type(point))

empty_tuple = ()
print(type(empty_tuple))

tuple2 = (1, 2) * 4
print(tuple2)

tuple3 = (1, 2) + (3, 4)
print(tuple3)

tuple3 = tuple("Hello")
print(tuple3)

tuple4 = (1, 2, 3, 4)
print(tuple4[1])
print(tuple4[1:3])
a, b, c, d = tuple4
print(a, b, c, d)

# Error -> tuple4[1] = 9