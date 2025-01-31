#Program for Obtaining Connection from Oracle DB
#OracleConnTestEx1.py
import oracledb as orc # Step-1
try:
    conn=orc.connect("system/manager@localhost/orcl") # Step-2
    print("Python Program got connection from Oracle Database")
    print("Type of conn=",type(conn))
except orc.DatabaseError as db:
    print("Problem with Oracle :",db)

