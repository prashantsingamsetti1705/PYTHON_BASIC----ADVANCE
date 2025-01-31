#Program for Deleting the Record  from employee table
#MySQLDeleteRecordEx.py
import mysql.connector
def deleterecord():
    while(True):
        try:
            con = mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="root",
                                          database="batch9am")  # Step-2
            cur=con.cursor()
            #Accept employee Number
            empno=int(input("Enter Employee Number:"))
            dq="delete from employee where eno=%d" %empno
            cur.execute(dq)
            con.commit()
            if(cur.rowcount>0):
                print("{} Record Deleted".format(cur.rowcount))
            else:
                print("Record Does not Exist")
            print("----------------------------------------")
            ch=input("Do u want to delete another record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for using this Program")
                break
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL DB:",db)
        except ValueError:
            print("Don't enter alnums,strs and symbols form employee Number")
#Main Program
deleterecord() # Function Call