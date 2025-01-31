#Program for Reading Student Data from KBD and Save them in Student Table by using Classes and Obejcts
#StudentOopWithOracle.py
import sys
class InvalidNameError(Exception):pass
class ZeroLengthError(BaseException):pass
class SpaceNameError(Exception):pass
import oracledb as orc
def validation(name):
    if(len(name)==0):
        raise ZeroLengthError
    elif(name.isspace()):
        raise SpaceNameError
    else:
            words = name.split()
            res = True
            for word in words:
                if (not word.isalpha()):
                    res = False
                    break
            if (res):
               return name
            else:
               raise InvalidNameError
class Student:
    def readstuddata(self):
        try:
            self.sno=int(input("Enter Student Number:"))
            self.name=validation(input("Enter Student Name:"))
            self.marks=float(input("Enter Student Marks:"))
        except ValueError:
            print("\tDon't enter alnums,symbols and strs for sno and marks")
        except InvalidNameError:
            print("\tInvalid Name and Try again")
        except SpaceNameError:
            print("Don't enter space for Name")
        except ZeroLengthError:
            print("Enter Ur Name")
        else:
            self.dispstuddata()

    def dispstuddata(self):
        print("="*50)
        print("Student Number:{}".format(self.sno))
        print("Student Name:{}".format(self.name))
        print("Student Marks:{}".format(self.marks))
        print("=" * 50)
        self.savestuddata()

    def savestuddata(self):
        try:
            con=orc.connect("system/manager@localhost/orcl")
            cur=con.cursor()
            iq="insert into student values(%d,'%s',%f)"
            cur.execute(iq %(self.sno,self.name,self.marks))
            con.commit()
            print("{} Student Record Inserted Sucessfully".format(cur.rowcount))
        except orc.DatabaseError as db:
            print("Problem with Oracle DB:",db)

#Main Program
s=Student()
s.readstuddata()