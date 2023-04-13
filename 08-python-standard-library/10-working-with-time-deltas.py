from datetime import datetime, timedelta

date = datetime(2023, 1, 1)
today = datetime.now()

duration = today - date
print(f"duration: {duration}")
print(f"days: {duration.days}")
print(f"seconds: {duration.seconds}")
print(f"total seconds: {duration.total_seconds()}")

print("-------------------------")
date2 = date + timedelta(days=365)
print(date2)