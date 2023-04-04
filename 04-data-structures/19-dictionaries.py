point = {"x": 4, "y": 8}
print(type(point))
point2 = dict(x=4, y=8)
print(type(point2))
print(point2["x"])
point2["x"] = 12
point2["z"] = 16
print(point2)

if "a" in point2:
    print("exists")
print("Exists a?", point2.get("a"))

del(point2["z"])
print(point2)

for key in point2:
    print(key)
for item in point2.items():
    print(item) #tuple
for key, value in point2.items():
    print(key, value)