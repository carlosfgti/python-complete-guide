try:
    age = int(input("Age: "))
    print("Your age is:", age)
except ValueError:
    print("You didn't enter a valid age.")
else:
    print("Congratulations")

print("Done")