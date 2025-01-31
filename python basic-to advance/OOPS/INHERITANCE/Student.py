#Student.py<---File Name and Module Name
import College
import mysql.connector
class Student(College.College):
    def getstuddet(self):
        self.sno=int(input("Enter Student Number:"))
        self.name=input("Enter Student Name:")
        self.crs=input("Enter Student Course:")
        self.getcolldet()
        self.getunivdet()
    def dispstuddet(self):
        self.dispunivdet()
        self.dispcolldet()
        print("-"*50)
        print("\t\tStudent Details")
        print("-" * 50)
        print("\t\tStudent Number:{}".format(self.sno))
        print("\t\tStudent Name:{}".format(self.name))
        print("\t\tStudent Course:{}".format(self.crs))
        print("-" * 50)
        self.savestuddata()
    def savestuddata(self):
        try:
            con=mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="root",
                                        database="batch9am")
            cur=con.cursor()
            #Query
            iq="insert into studres values(%d,'%s','%s','%s','%s','%s','%s') "
            cur.execute(iq %(self.sno,self.name,self.crs,self.cname,self.cloc,self.uname,self.uloc))
            con.commit()
            print("{} Student Record Inserted".format(cur.rowcount))
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL:",db)
