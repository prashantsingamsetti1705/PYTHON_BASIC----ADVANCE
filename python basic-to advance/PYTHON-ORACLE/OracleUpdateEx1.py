#Program for Updating the Salary of all employee by 10% Hike
#OracleUpdateEx1.py
import oracledb as orc
def updaterecord():
    try:
        con = orc.connect("system/manager@127.0.0.1/orcl")
        cur = con.cursor()
        cur.execute("update employee set sal=sal+sal*10/100")
        con.commit()
        print("{} Employee Records Updated".format(cur.rowcount))
    except orc.DatabaseError as db:
        print("Problem in Oracle DB:", db)

#Main Program
updaterecord() # Function Call