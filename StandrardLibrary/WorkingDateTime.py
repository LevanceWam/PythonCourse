from datetime import datetime
import time
# gives us the month, year or the day we can also do the hour, minute, second of the day

dt = datetime(2018, 1, 1)
# gives us the current date
dt = datetime.now()
# converting a date time string
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())
print(dt)

print(f"{dt.year}/{dt.month}")
# formatting datetime
# opposite of strptime
# we convert the time into a string
print(dt.strftime("%Y/%m"))
