#Program for Getting the Records from any Table along with Col Names
#OracleColumnsWithRecordsByOrder.py
import oracledb as orc
def selectcolwithrecords():
    try:
        con=orc.connect("system/manager@localhost/orcl")
        cur=con.cursor()
        #Read the records from employee Table
        sq="select * from employee order by eno desc"
        cur.execute(sq)
        print("-------------------------------------------------")
        #To get the col names, we use an attribute description present in cursor object
        #Code for Getting the Column Names
        metadata=cur.description
        for colinfo in metadata:
            print(colinfo[0],end="\t\t")
        print()
        print("-------------------------------------------------")
        #Cde for Getting the Records
        records=cur.fetchall()
        for record in records:
            for val in record:
                print("{}".format(val),end="\t\t")
            print()
        print("-------------------------------------------------")
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:",db)

#Main Program
selectcolwithrecords()
