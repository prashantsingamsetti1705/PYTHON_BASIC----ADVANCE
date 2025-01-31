#ClassLevelMethodEx4.py
class Employee:
    @classmethod
    def getcompname(cls):# Class Level Method Name
        cls.compname="IBM" # OR Employee.compname="IBM"
        # Here compname is called Class Level Data Member
        cls.getcity() # OR Employee.getcity()
    @classmethod
    def getcity(cls):  # Class Level Method Name
        cls.city="HYD"   # Employee.city="HYD"
        #Here city is called Class Level Data Member
    def getempdetails(self):
        self.eno=int(input("Enter Employee Number:"))
        self.name=input("Enter Employee Name:")
        self.sal=float(input("Enter Employee Salary:"))
        self.dispempvals() # Calling Instance method
    def dispempvals(self):
        print("="*50)
        print("\tEmployee Number:{}".format(self.eno))
        print("\tEmployee Name:{}".format(self.name))
        print("\tEmployee Salary:{}".format(self.sal))
        print("\tEmployee Comp Name:{}".format(Employee.compname))
        print("\tEmployee Comp City:{}".format(Employee.city))
        print("=" * 50)
#Main Program
Employee.getcompname() # calling Class Level Method w.r.t Class Name
#Create an object of Employee object
eo=Employee()
eo.getempdetails()
