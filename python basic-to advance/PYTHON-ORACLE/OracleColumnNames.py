#Program for Getting the Column Names of table
#OracleColumnNames.py
import oracledb as orc
def selectcolnames():
    try:
        con=orc.connect("system/manager@localhost/orcl")
        cur=con.cursor()
        #Read the records from employee Table
        sq="select * from employee"
        cur.execute(sq)
        print("-------------------------------------------------")
        #To get the col names, we use an attribute description present in cursor object
        metadata=cur.description
        for colinfo in metadata:
            print(colinfo[0],end="\t\t")
        print()
        print("-------------------------------------------------")
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#Main Program
selectcolnames()
