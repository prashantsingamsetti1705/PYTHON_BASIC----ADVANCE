#StaticMethodEx5.py
class Emp:
    def getempvals(self):
        self.eno=int(input("Enter Employee Number:"))
        self.name = input("Enter Employee Name:")
        self.sal=float(input("Enter Employee Salary:"))

class Student:
    def getstudvals(self):
        self.sno = int(input("Enter Student Number:"))
        self.name = input("Enter Student Name:")

class Teacher:
    def getteachervals(self):
        self.tno=int(input("Enter Teacher Number:"))
        self.name = input("Enter Teacher Name:")
        self.exp=float(input("Enter Teacher Exp:"))
        self.subject=input("Enter Teacher Subject:")
class HYD:
    def dispobjdata(self,obj,objinfo):
       self.dispobjdata(obj,objinfo) # Calling Static Method from Class Level Method w.r.t cls

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
HYD().dispobjectdata(e,"Employee") # Calling Instance Method w.r.t  Name-Less Method
HYD().dispobjectdata(s,"Student") # Calling Instance Method w.r.t  Name-Less Method
HYD().dispobjectdata(t,"Teacher") # Calling Instance Method w.r.t  Name-Less Method