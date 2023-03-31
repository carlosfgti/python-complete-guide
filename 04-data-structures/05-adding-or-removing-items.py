letters = ["a", "b", "c", "d"]

# Add
letters.append("e")
letters.insert(0, "->")
letters.insert(len(letters), "<-")
print(letters)

# Remove
letters.pop() # remove last
letters.pop(0)
letters.remove("c") # remove first occurrence 
del letters[0:2]
print(letters)