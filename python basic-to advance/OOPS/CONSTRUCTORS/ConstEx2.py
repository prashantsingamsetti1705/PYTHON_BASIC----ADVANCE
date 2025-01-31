#ConstEx2.py
class Student:
    def __init__(self,sno,sname): # Parametrized Constructor
        print("I am from  Parametrized Constructor")
        self.sno=sno
        self.name=sname

#Main Program
s1=Student(100,"Travis") # Object Creation--Makes the PVM to call Constructor Automatically OR Implocitly
print("Content of s1=",s1.__dict__)
s2=Student(200,"Jhunter") # Object Creation--Makes the PVM to call Constructor Automatically OR Implocitly
print("Content of s2=",s2.__dict__)
s3=Student(300,"Rossum") # Object Creation--Makes the PVM to call Constructor Automatically OR Implocitly
print("Content of s3=",s3.__dict__)