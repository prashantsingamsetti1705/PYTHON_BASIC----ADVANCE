#Program for Inserting a Record in the employee table
#OracleInsertRecordEx1.py
import oracledb as orc # Step-1
def insertrecord():
    try:
        con=orc.connect("system/manager@localhost/orcl") #Step-2
        cur=con.cursor() # Step-3
        #Step-4
        iq="insert into employee values(104,'Younis',1.3,'Wipro')"
        cur.execute(iq) # Step-5
        con.commit()
        print("Employee Record Inserted Sucessfully") #Step-6

    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#Main Program
insertrecord() # Function Call