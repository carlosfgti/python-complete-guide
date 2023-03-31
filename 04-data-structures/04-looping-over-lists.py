letters = ["a", "b", "c", "d"]
for letter in letters:
    print(letter)
print("-----------------------")
for letter in enumerate(letters):
    print(letter)
    print("index", letter[0])
    print("value", letter[1])
    index, value = letter
    print(index, value)
print("-----------------------")
for index, value in enumerate(letters):
    print(index, value)