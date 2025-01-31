#Program for Deleting the Record  from employee table
#OracleDeleteEx2.py
import oracledb as orc
def deleterecord():
    while(True):
        try:
            con=orc.connect("system/manager@127.0.0.1/orcl")
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
        except orc.DatabaseError as db:
            print("Problem in Oracle DB:",db)
        except ValueError:
            print("Don't enter alnums,strs and symbols form employee Number")
#Main Program
deleterecord() # Function Call