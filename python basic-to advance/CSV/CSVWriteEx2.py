#Program for Adding the Record to CSV File
#CSVWriteEx2.py
import csv
record=[106,"Rossum",9.6,"NLU"]
with open("E:\\KVR-PYTHON-9AM\\CSV\\NOTES\\student.csv","a") as fp:
    csvwr=csv.writer(fp)
    csvwr.writerow(record)
    print("Record addded to CSV File--verity")