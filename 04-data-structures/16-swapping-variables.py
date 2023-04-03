a = 2
b = 4
print("a = ", a)
print("b = ", b)

# old
c = a
a = b
b = c
print("a = ", a)
print("b = ", b)

# new
a, b = b, a
print("a = ", a)
print("b = ", b)