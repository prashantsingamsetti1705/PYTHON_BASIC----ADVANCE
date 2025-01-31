#Program for Getting Current Date and Time
#CurrentTimeEx.py
import datetime
tdt=datetime.datetime.now()
print("Current Date and Time")
print(tdt,type(tdt))
print("-----------------------------------------------------------")
print("Hour in 24 HRS Format=",tdt.strftime("%H"))  
print("Hour in 12 HRS format=",tdt.strftime("%I"))  
print("are u in AM OR PM=",tdt.strftime("%p"))  
print("Minutes=",tdt.strftime("%M"))  
print("Second=",tdt.strftime("%S"))  
print("Micro Seconds=",tdt.strftime("%f"))  
print("-----------------------------------------------------------")
print("Day Number of Year=",tdt.strftime("%j"))  
print("Week Number of Year-Sunday staring=",tdt.strftime("%U"))  
print("Week Number of Year-Monday starting=",tdt.strftime("%W"))  
print("Century=",tdt.strftime("%C"))  
print("local date=",tdt.strftime("%x"))  
print("Local Version of Time=",tdt.strftime("%X"))  
print("Week Number=",tdt.strftime("%V"))  
print("Week Day According to ISO 8601=",tdt.strftime("%u"))  



