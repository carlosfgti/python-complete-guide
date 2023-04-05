try:
    with open("app.log", "+a") as file_reports:
        print("File opened + created")

    age = int(input("Age: "))
    age_half = 2 / age
except (ValueError, ZeroDivisionError):
    print("Error.")
else:
    print("Perfect!")