#Program for Reading the Data from CSV File without using csv module
#CSVDictReadEx1.py
import csv
with open("E:\\KVR-PYTHON-9AM\\CSV\\NOTES\\employee.csv","r") as fp:
    csvdr=csv.DictReader(fp) # here csvdr is an object of <class 'csv.DictReader'>
    recno=1
    for recdict in csvdr:
        print("\tRecord:{}".format(recno))
        for k,v in recdict.items():
            print("\t\t{}--->{}".format(k,v))
        print("-------------------------------------")
        recno=recno+1



