#Program for Reading the Records from employee table--by using fetchmany()
#OracleSelectRecordEx2.py
import oracledb as orc
def selectrecords():
    try:
        con=orc.connect("system/manager@localhost/orcl")
        cur=con.cursor()
        #Read the records from employee Table
        sq="select * from employee"
        cur.execute(sq)
        records=cur.fetchmany(4)
        print("------------------------------------------")
        for record in records:
            for val in record:
                print("{}".format(val),end="\t\t")
            print()
        print("------------------------------------------")
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#Main Program
selectrecords()