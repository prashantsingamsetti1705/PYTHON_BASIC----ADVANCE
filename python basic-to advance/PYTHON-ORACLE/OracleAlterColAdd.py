#Program for adding the new column name to Employee Table
#OracleAlterColAdd.py
import oracledb as orc
def alteratblecoladd():
    try:
        con=orc.connect("system/manager@localhost/orcl") # Step-2
        cur=con.cursor() # Step-3
        #Step-4
        aqa="alter table employee add(compname varchar2(10))"
        cur.execute(aqa)
        print("New Column Name added Sucessfully--verify") # Step-5
    except orc.DatabaseError as db:
        print("Probelm in Oracle:",db) # Step-5
#Main Program
alteratblecoladd() # function call