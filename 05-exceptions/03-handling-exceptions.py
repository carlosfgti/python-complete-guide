try:
    age = int(input("Age: "))
    print("Your age is:", age)
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("Congratulations")

print("Done")