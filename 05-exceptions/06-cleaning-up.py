try:
    file_reports = open("reports.csv")
    age = int(input("Age: "))
    age_half = 2 / age
except (ValueError, ZeroDivisionError):
    print("Error")
    # file_reports.close()
else:
    print("Perfect!")
    # file_reports.close()
finally:
    file_reports.close()