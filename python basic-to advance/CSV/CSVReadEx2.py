#Program for Reading the Data from CSV File without using csv module
#CSVReadEx1.py
import csv
with open("E:\\KVR-PYTHON-9AM\\CSV\\NOTES\\student.csv","r") as fp:
    csvr=csv.reader(fp) # Here csvr is an object of <class, _csv.reader>
    for record in csvr: # here record is an object of <class, list>
        for val in record:
            print("\t{}".format(val),end="\t")
        print()


