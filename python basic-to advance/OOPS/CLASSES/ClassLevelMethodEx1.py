#ClassLevelMethodEx1.py
class Employee:
    @classmethod
    def getvalues(cls):
        cls.compname="IBM" # OR Employee.compname="IBM"
        cls.city="HYD"   # Employee.city="HYD"
        #Here compname and city are called Class Level Data Members

#Main Program
Employee.getvalues() # Calling Class Level method w.r.t Class Name
print("Comp Name=",Employee.compname) # Accessing Class Level Data Members w.r.t Class Name
print("Comp Located City=",Employee.city) # Accessing Class Level Data Members w.r.t Class Name
print("------------------------------------------")
#Create an object of Employee
eo=Employee()
print("Content of eo=",eo.__dict__)
print("Comp Name=",eo.compname)# Accessing Class Level Data Members w.r.t Object Name
print("Comp Located City=",eo.city)# Accessing Class Level Data Members w.r.t Object Name

