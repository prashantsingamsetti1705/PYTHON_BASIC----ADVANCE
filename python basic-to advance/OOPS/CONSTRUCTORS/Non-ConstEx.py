#Non-ConstEx.py
class Student:
    def getstuddata(self):
        self.sno=100
        self.name="Rossum"

#Main Program
s=Student()
print("Content of s=",s.__dict__) # { }
s.getstuddata() #Normal Method--Calling Explicitly for placing Instance Data Members
print("Content of s=",s.__dict__) # {"sno":100,"name":"Rossum}