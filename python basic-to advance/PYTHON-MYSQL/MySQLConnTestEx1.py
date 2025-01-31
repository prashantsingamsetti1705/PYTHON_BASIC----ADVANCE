#Program for Obtaining the connection from MySQL
#MySQLConnTestEx1.py
import mysql.connector # Step-1
try:
    con=mysql.connector.connect(host="localhost",
                                user="root",
                                passwd="root") #Step-2
    print("Python Program got connection from MySQL")
except mysql.connector.DatabaseError:
    print("Problem in MySQL Connection")
