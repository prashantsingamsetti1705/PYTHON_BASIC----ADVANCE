#Program for Deleting the Record  from employee table
#OracleDeleteEx1.py
import oracledb as orc
def deleterecord():
    try:
        con=orc.connect("system/manager@127.0.0.1/orcl")
        cur=con.cursor()
        dq="delete from employee where eno=105"
        cur.execute(dq)
        con.commit()
        print("{} Record Deleted".format(cur.rowcount))
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#Main Program
deleterecord() # Function Call