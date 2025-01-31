#DiffBetweenDates.py
import datetime
x = datetime.datetime(2022, 12, 24)
print("Old Date=",x) 
td=datetime.datetime.now()
dt=td-x
print("Difference between dates=",dt)
print("Type of dt=",type(dt))
print("--------------------------------------------------------")
datetime1 = datetime.datetime(2023, 10, 1, 8, 15, 25)
datetime2 =datetime.datetime(2023, 9, 28, 12, 0, 0)
difference = datetime1 - datetime2
print("Difference between dates=",difference)
print("--------------------------------------------------------")
date1 = datetime.date(2023, 10, 1)
date2 = datetime.date(2023, 9, 28)
difference = date1 - date2
print("Difference between dates=",difference)