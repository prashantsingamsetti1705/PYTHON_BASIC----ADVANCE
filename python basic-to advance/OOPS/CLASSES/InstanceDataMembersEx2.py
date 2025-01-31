#Program for Storing Sno,name and marks by using Classes and Objects
#InstanceDataMembersEx2.py
class Student:pass

#main program
s1=Student() # Student Object Creation
s2=Student() # Student Object Creation
print("Content of s1=",s1.__dict__)
print("Content of s2=",s2.__dict__)
print("Number of Values in s1=",len(s1.__dict__))
print("Number of Values in s2=",len(s2.__dict__))
print("----------------------------------------------")
#Palce Instance Data Members in S1
s1.sno=100
s1.name="Rossum"
s1.marks=45.67 # Here sno,name and marks are called Instance Data Members
#Palce Instance Data Members in S2
s2.sno=200
s2.name="Travis"
s2.marks=77.77
print("Content of s1=",s1.__dict__)
print("Content of s2=",s2.__dict__)
print("Number of Values in s1=",len(s1.__dict__))
print("Number of Values in s2=",len(s2.__dict__))
print("----------------------------------------------")
#Display the Object Data of S1
print("Content of s1 Object")
for dmn,dmv in s1.__dict__.items():
    print("\t{}---->{}".format(dmn,dmv))
print("----------------------------------------------")
#Display the Object Data of S2
print("Content of s2 Object")
for dmn in s2.__dict__.keys():
    print("\t{}----->{}".format(dmn,s2.__dict__.get(dmn)))
print("----------------------------------------------")