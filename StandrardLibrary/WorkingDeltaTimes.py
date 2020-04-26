from datetime import datetime, timedelta

dt1 = datetime(2019, 1, 1) + timedelta(days=1, seconds=1000)
dt2 = datetime.now()
print(dt1)
duration = dt2 - dt1
print(duration)
print("Days: ", duration.days)
print("Seconds: ", duration.seconds)
print("Seconds:", duration.total_seconds())
