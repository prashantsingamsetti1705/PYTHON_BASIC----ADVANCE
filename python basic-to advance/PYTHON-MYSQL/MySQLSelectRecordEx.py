#Program for Getting the Records from any Table along with Col Names
#MySQLSelectRecordEx.py
import mysql.connector
def selectcolwithrecords():
    try:
        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="root",
                                      database="batch9am")  # Step-2
        cur=con.cursor()
        #Read the records from employee Table
        sq="select * from employee order by sal"
        cur.execute(sq)
        print("-------------------------------------------------")
        #To get the col names, we use an attribute description present in cursor object
        #Code for Getting the Column Names
        metadata=cur.description
        for colinfo in metadata:
            print(colinfo[0],end="\t\t")
        print()
        print("-------------------------------------------------")
        #Cde for Getting the Records
        records=cur.fetchall()
        for record in records:
            for val in record:
                print("{}".format(val),end="\t\t")
            print()
        print("-------------------------------------------------")
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQL DB:",db)

#Main Program
selectcolwithrecords()
