#Program for Getting Current Date and Time
#CurrentDateTimeEx.py
import datetime
tdt=datetime.datetime.now()
print("Current Date and Time")
print(tdt,type(tdt))
print("-----------------------------------------------------------")
print("Week Name in short=",tdt.strftime("%a"))  
print("Week Name in Full Version=",tdt.strftime("%A"))  
print("Week Number=",tdt.strftime("%w"))  
print("Day Number=",tdt.strftime("%d"))  
print("Month Name in short=",tdt.strftime("%b"))  
print("Month Name in Full Version=",tdt.strftime("%B"))  
print("Month Number=",tdt.strftime("%m"))  
print("Year  Number without century=",tdt.strftime("%y"))  
print("Year  Number with century=",tdt.strftime("%Y"))  
