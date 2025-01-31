#Program for Creating CSV File with Dict Data.
#CSVDictWriteEx1.py
import csv # Step-1
colnames=["TNO","NAME","SUBJECT"] # Step-2
records=[{"TNO":1000,"NAME":"ROSSUM","SUBJECT":"PYTHON"},
         {"TNO":2000,"NAME":"TRAVIS","SUBJECT":"NUMPY"},
         {"TNO":3000,"NAME":"HUNTER","SUBJECT":"MATPLOTLIB"},
         {"TNO":4000,"NAME":"DENNIS","SUBJECT":"C"},
         {"TNO":5000,"NAME":"JGOSLING","SUBJECT":"JAVA"} ] # Step-3
with open("E:\\KVR-PYTHON-9AM\\CSV\\NOTES\\teacher.csv","a") as fp: # Step-4
     csvdwr=csv.DictWriter(fp,fieldnames=colnames) # Step-5
     csvdwr.writeheader() # Step-6
     csvdwr.writerows(records) # Step-7
     print("CSV File Created with Dict Data---verify")
