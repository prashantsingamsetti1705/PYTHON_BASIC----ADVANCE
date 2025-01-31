#Program for Creating Database Name as "batch9am"
#MySQLDataBaseCreateEx.py
import mysql.connector # Step-1
def databasecreate():
    try:
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="root") # Step-2
        cur=con.cursor() #Step-3
        #Step-4
        dc="create database batch9am"
        cur.execute(dc)
        print("Database created in MySQL Sucessfully--verify")  # Step-5
    except mysql.connector.DatabaseError as db:
        print("Probem with MySQL:", db)

#Main Program
databasecreate() # Funcion Call