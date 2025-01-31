#Program for Updating   sal and comp name of   employee
#MySQLUpdateRecordEx.py
import mysql.connector
def updaterecord():
    while(True):
        try:
            con = mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="root",
                                          database="batch9am")  # Step-2
            cur=con.cursor()
            #Accept employee Number
            empno=int(input("Enter Employee Number for Updating Sal and Comp Name:"))
            empsal=float(input("Enter New Salary for Employee:"))
            cname=input("Enter New Comp Name of Employee:")
            uq="update employee set sal=%f,compname='%s' where eno=%d" %(empsal,cname,empno)
            cur.execute(uq)
            con.commit()
            if(cur.rowcount>0):
                print("{} Record Updated".format(cur.rowcount))
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
updaterecord() # Function Call