try:
    age = int(input("Age: "))
    age_half = 2 / age
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
except ZeroDivisionError:
    print("Age cannot be zero.")
else:
    print("Congratulations.")

print("Done.")