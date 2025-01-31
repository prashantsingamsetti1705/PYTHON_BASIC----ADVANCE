#Program for Demonstrating the Need of Class Level Data Members
#ClassLevelDataMemberEx1.py
class Student:
    crs="PYTHON"
    city="HYD" # Here crs and city are called Class Level Data Members

#Main Program
s=Student()
print("Student content=",s.__dict__ )
#Class Level Data Members are Not avauilable with Object
#Access the Values of Class Level Data Members
print("Student Course=",Student.crs)
print("Student City=",Student.city)
print("-------------OR---------------------")
print("Student Course=",s.crs)
print("Student City=",s.city)
