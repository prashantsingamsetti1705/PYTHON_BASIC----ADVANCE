#Program for Creating an object of cursor
#MySQLCursorEx.py
import mysql.connector # Step-1
try:
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                passwd="root") # Step-2
    print("Python Program got connection from MySQL")
    print("-------------------------------------------")
    cur=con.cursor() #Step-3
    print("Python Program created Cursor object")
except mysql.connector.DatabaseError:
    print("Probem with MySQL")
