letters = ["a", "b", "c", "d"]
print(letters.index("c"))
# print(letters.index("e")) # error

print(letters.count("e"))
if "e" in letters:
    print(letters.index("e"))