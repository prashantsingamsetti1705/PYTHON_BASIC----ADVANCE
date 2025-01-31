#Program for Creating CSV File
#CSVWriteEx1.py
import csv
#Take Column Names--Step-1
colnames=["SNO","NAME","MARKS","COLNAME"]
#Step-2---Choose the Records
Records=[[100,"Praveen",2.3,"XYZ"],
        [101,"Rajesh",3.3,"PQR"],
        [102,"Ramesh",5.3,"ABC"],
        [103,"Raja",4.3,"KLM"],
        [104,"Sachin",1.3,"XAB"] ]
#Choose CSV File and Open it into write mode--Step-3
with open("E:\\KVR-PYTHON-9AM\\CSV\\NOTES\\student.csv","a") as fp:
    csvwr=csv.writer(fp) # here csvwr is an object of <class, _csv.writer>--Step-4
    csvwr.writerow(colnames) # Step-5
    csvwr.writerows(Records) # Stecp-6
    print("CSV File Created--Verify")
