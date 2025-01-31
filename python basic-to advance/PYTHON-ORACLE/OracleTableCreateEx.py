#Program for Creating Table "Employee"
#OracleTableCreateEx.py
import oracledb as orc # Step-1
def tablecreate():
    try:
        con=orc.connect("system/manager@localhost/orcl") # Step-2
        cur=con.cursor() # Step-3
        #Step-4
        ctq="create table kvr(cno number(2) primary key,cname varchar2(10) not null)"
        cur.execute(ctq)
        print("Table created Sucessfully--verify") # Step-5
    except orc.DatabaseError as db:
        print("Probelm in Oracle:",db) # Step-5

#Main Program
tablecreate() # function call