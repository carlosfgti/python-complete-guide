import csv
from pathlib import Path

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "price"])
    writer.writerow([1, "prod1", 20.2])
    writer.writerows([
        [2, "prod2", 22.2],
        [3, "prod3", 33.3],
        [4, "prod4", 44.4],
    ])

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

Path("data.csv").unlink()