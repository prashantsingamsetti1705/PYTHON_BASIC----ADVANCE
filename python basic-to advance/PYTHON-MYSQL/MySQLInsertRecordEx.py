#Program for Inserting a Record in the employee table
#MySQLInsertRecordEx.py
import mysql.connector # Step-1
def insertrecord():
    while(True):
        try:
            con = mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="root",
                                          database="batch9am")  # Step-2
            cur=con.cursor() # Step-3
            #Read Employee Values from Key Board
            print("---------------------------------------------")
            empno=int(input("Enter Employee Number:"))
            empname=input("Enter Employee Name:")
            empsal=float(input("Enter Employee Salary:"))
            cname=input("Enter Employee Comp Name:")
            #Step-4
            iq="insert into employee values(%d,'%s',%f,'%s')"
            cur.execute(iq %(empno,empname,empsal,cname)) # Step-5
            con.commit()
            print("---------------------------------------------")
            print("{} Employee Record Inserted Sucessfully".format(cur.rowcount)) #Step-6
            print("---------------------------------------------------")
            ch=input("Do u want insert Another Record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for using this Program")
                break
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL DB:",db)
        except ValueError:
            print("Don't enter alnums,strs and symbols for empno,salary")
#Main Program
insertrecord() # Function Call