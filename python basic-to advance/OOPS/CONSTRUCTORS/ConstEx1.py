#ConstEx1.py
class Student:
    def __init__(self): # Default OR Parameter-Less Constructor
        print("I am from Default  Constructor")
        self.sno=100
        self.name="Rossum"


#Main Program
s1=Student() # Object Creation--Makes the PVM to call Constructor Automatically OR Implocitly
print("Content of s1=",s1.__dict__)
s2=Student() # Object Creation--Makes the PVM to call Constructor Automatically OR Implocitly
print("Content of s2=",s2.__dict__)
s3=Student() # Object Creation--Makes the PVM to call Constructor Automatically OR Implocitly
print("Content of s3=",s3.__dict__)