#Program for changing the column sizes of Employee Table
#OracleAlterColSizes.py
import oracledb as orc
def alteratblecolsizes():
    try:
        con=orc.connect("system/manager@localhost/orcl") # Step-2
        cur=con.cursor() # Step-3
        #Step-4
        aqc="alter table employee modify(eno number(3), name varchar2(15))"
        cur.execute(aqc)
        print("Table  column sizes altered Sucessfully--verify") # Step-5
    except orc.DatabaseError as db:
        print("Probelm in Oracle:",db) # Step-5

#Main Program
alteratblecolsizes() # function call