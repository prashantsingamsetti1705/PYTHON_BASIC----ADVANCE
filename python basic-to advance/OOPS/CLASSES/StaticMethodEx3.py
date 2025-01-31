#StaticMethodEx3.py
class Emp:
    def getempvals(self):
        self.eno=int(input("Enter Employee Number:"))
        self.name = input("Enter Employee Name:")
        self.sal=float(input("Enter Employee Salary:"))
        #Calling Static Method of HYD class from Instance Method of Emp
        HYD.dispobjectdata(self,"Employee")

class Student:
    def getstudvals(self):
        self.sno = int(input("Enter Student Number:"))
        self.name = input("Enter Student Name:")
        # Calling Static Method of HYD class from Instance Method of Emp
        HYD.dispobjectdata(self, "Student")

class Teacher:
    def getteachervals(self):
        self.tno=int(input("Enter Teacher Number:"))
        self.name = input("Enter Teacher Name:")
        self.exp=float(input("Enter Teacher Exp:"))
        self.subject=input("Enter Teacher Subject:")
        # Calling Static Method of HYD class from Instance Method of Emp
        HYD.dispobjectdata(self, "Teacher")
class HYD:
    @staticmethod
    def dispobjectdata(obj,objinfo):
        print("---------------------------------")
        print("{} Object Information".format(objinfo))
        print("---------------------------------")
        for dmn,dmv in obj.__dict__.items():
            print("\t{}--->{}".format(dmn,dmv))
        print("---------------------------------")


#Main Program
e=Emp()
s=Student()
t=Teacher()
e.getempvals()
print("-----------------------------------------")
s.getstudvals()
print("-----------------------------------------")
t.getteachervals()
print("-----------------------------------------")

