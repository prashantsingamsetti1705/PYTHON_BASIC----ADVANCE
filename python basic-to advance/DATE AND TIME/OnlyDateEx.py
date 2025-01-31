# Python program to print current date
#OnlyDateEx.py
from datetime import date

# calling the today  function of date class
today = date.today()
print("Today's date is", today)  # Today's date is 2024-12-24
print("Current year:", today.year) # Current year: 2024
print("Current month:", today.month) # Current month: 12
print("Current day:", today.day) # Current day: 24