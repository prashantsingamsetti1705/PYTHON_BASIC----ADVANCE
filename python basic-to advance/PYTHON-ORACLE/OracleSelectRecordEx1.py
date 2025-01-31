#Program for Reading the Records from employee table--by using fetchone()
#OracleSelectRecordEx1.py
import oracledb as orc
def selectrecords():
    try:
        con=orc.connect("system/manager@localhost/orcl")
        cur=con.cursor()
        #Read the records from employee Table
        sq="select * from employee"
        cur.execute(sq)
        print("------------------------------------")
        while(True):
            record = cur.fetchone()
            if(record!=None):
                for val in record:
                    print("{}".format(val),end="\t\t")
                print()
            else:
                print("------------------------------------")
                break
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#Main Program
selectrecords()