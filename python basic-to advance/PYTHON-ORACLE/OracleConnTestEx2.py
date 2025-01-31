#Program for Obtaining Connection from Oracle DB
#OracleConnTestEx2.py
import oracledb as orc # Step-1
try:
    conn=orc.connect("system/manager@127.0.0.1/orcl") # Step-2
    print("Python Program got connection from Oracle Database")
    print("Type of conn=",type(conn))
except orc.DatabaseError as db:
    print("Problem with Oracle :",db)

