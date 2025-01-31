#Program for Demonstrating the Cursor Object Creation
#OracleCursor.py
import oracledb as orc # Step-1
try:
    conn=orc.connect("system/manager@localhost/orcl") # Step-2
except orc.DatabaseError as db:
    print("Problem with Oracle Connection")
else:
    print("Python Program got connection from Oracle Database")
    print("Type of conn=", type(conn))
    print("---------------------------------------------------")
    cur = conn.cursor()  # Step-3
    print("Python Program created Cursor Object")
    print("Type of cur=", type(cur))
    print("---------------------------------------------------")
finally:
    try:
        print("I am from Finally Block")
        conn.close()
        print("Database Connection Closed")
    except NameError:
        print("Connection not at all established---no need to close")