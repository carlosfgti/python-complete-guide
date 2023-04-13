from datetime import datetime
import time

dt = datetime(2023, 1, 1)
print(dt)
print(datetime.now())

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
print(datetime.strptime("2023/02/21", "%Y/%m/%d"))

date = datetime.fromtimestamp(time.time())
print(date)
print(f"{date.day}/{date.month}/{date.year}")
print(date.strftime("%d/%m/%Y"))