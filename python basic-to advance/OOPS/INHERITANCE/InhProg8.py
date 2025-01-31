#InhProg8.py
import mysql.connector
class University:
    def getunivdet(self):
        self.uname=input("Enter University Name:")
        self.uloc=input("Enter University Location:")
    def dispunivdet(self):
        print("-"*50)
        print("\t\tUniversity Details")
        print("-" * 50)
        print("\t\tUniversity Name:{}".format(self.uname))
        print("\t\tUniversity Location:{}".format(self.uloc))
        print("-" * 50)
class College(University):
    def getcolldet(self):
        self.cname = input("Enter College Name:")
        self.cloc = input("Enter College Location:")
    def dispcolldet(self):
        print("\t\tCollege Details")
        print("-" * 50)
        print("\t\tCollege Name:{}".format(self.cname))
        print("\t\tCollege Location:{}".format(self.cloc))
        print("-" * 50)
class Student(College):
    def getstuddet(self):
        self.sno=int(input("Enter Student Number:"))
        self.name=input("Enter Student Name:")
        self.crs=input("Enter Student Course:")
    def dispstuddet(self):
        print("-"*50)
        print("\t\tStudent Details")
        print("-" * 50)
        print("\t\tStudent Number:{}".format(self.sno))
        print("\t\tStudent Name:{}".format(self.name))
        print("\t\tStudent Course:{}".format(self.crs))
        print("-" * 50)
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

#Main Program
s=Student()
s.getstuddet()
s.getcolldet()
s.getunivdet()
s.dispunivdet()
s.dispcolldet()
s.dispstuddet()
s.savestuddata()
