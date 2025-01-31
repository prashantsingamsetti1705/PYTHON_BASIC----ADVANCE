#StaticMethodEx4.py
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
    @classmethod
    def dispobjdata(cls,obj,objinfo):
        cls.dispobjdata(obj,objinfo) # Calling Static Method from Class Level Method w.r.t cls
            #OR
        #HYD.dispobjdata(obj, objinfo)  # Calling Static Method from Class Level Method w.r.t cls
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
HYD.dispobjectdata(e,"Employee") # Calling Class Level Method w.r.t Class Name
HYD.dispobjectdata(s,"Student") # Calling Class Level Method w.r.t Class Name
HYD.dispobjectdata(t,"Teacher") # Calling Class Level Method w.r.t Class Name