#Program for Creating a Table in bartch9am Database
#MySQLTableCreateEx.py
import mysql.connector # Step-1
def tablecreate():
    try:
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="root",
                                    database="batch9am") # Step-2
        cur=con.cursor() #Step-3
        #Step-4
        tc="create table employee(eno int primary key,name varchar(10) not null, sal real not null,compname varchar(10) not null )"
        cur.execute(tc)
        print("Database created in MySQL Sucessfully--verify")  # Step-5
    except mysql.connector.DatabaseError as db:
        print("Probem with MySQL:", db)

#Main Program
tablecreate() # Funcion Call