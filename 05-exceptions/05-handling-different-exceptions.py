try:
    age = int(input("Age: "))
    age_half = 2 / age
except (ValueError, ZeroDivisionError) as ex:
    print(ex)
else:
    print("Congratulations.")

print("Done.")