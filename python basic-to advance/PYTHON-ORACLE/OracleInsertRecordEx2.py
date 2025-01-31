#Program for Inserting a Record in the employee table
#OracleInsertRecordEx2.py
import oracledb as orc # Step-1
def insertrecord():
    try:
        con=orc.connect("system/manager@localhost/orcl") #Step-2
        cur=con.cursor() # Step-3
        #Read Employee Values from Key Board
        empno=int(input("Enter Employee Number:"))
        empname=input("Enter Employee Name:")
        empsal=float(input("Enter Employee Salary:"))
        cname=input("Enter Employee Comp Name:")
        #Step-4
        iq="insert into employee values(%d,'%s',%f,'%s')"
        cur.execute(iq %(empno,empname,empsal,cname)) # Step-5
        con.commit()
        print("{} Employee Record Inserted Sucessfully".format(cur.rowcount)) #Step-6
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)
#Main Program
insertrecord() # Function Call