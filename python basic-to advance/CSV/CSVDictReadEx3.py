#Program for Reading the Data from CSV File without using csv module
#CSVDictReadEx3.py
import csv
with open("E:\\KVR-PYTHON-9AM\\CSV\\NOTES\\student.csv","r") as fp:
    csvdr=csv.DictReader(fp) # here csvdr is an object of <class 'csv.DictReader'>
    for dictrec in csvdr: # here dictrec is an object of <class, dict>
        for k,v in dictrec.items():
            print("\t{}-->{}".format(k,v))
        print()
        print("-"*50)
