#program for Reading and Displaying the Deatils students by using Classes and Objects
#InstanceMethodEx1.py
class Student:
    def readstuddata(self):
        print("Current Object Ref in IM=",id(self))

#main Program
s1=Student()
print("Content of s1 before reading=",s1.__dict__)
print("Memory ID of s1 in main program=",id(s1))
s1.readstuddata() # calling Instance Method
print("------------------------------------------")
s2=Student()
print("Content of s2 before reading=",s2.__dict__)
print("Memory ID of s2 in main program=",id(s2))
s2.readstuddata() # calling Instance Method

