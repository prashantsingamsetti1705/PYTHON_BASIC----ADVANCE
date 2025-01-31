#Program for Storing Sno,name and marks by using Classes and Objects
#InstanceDataMembersEx1.py
class Student:pass

#main program
s1=Student() # Student Object Creation
s2=Student() # Student Object Creation
print("ID of s1=",id(s1))
print("ID of s2=",id(s2))
print("----------------------------------")
#Palce Instance Data Members in S1
s1.sno=100
s1.name="Rossum"
s1.marks=45.67 # Here sno,name and marks are called Instance Data Members
#Palce Instance Data Members in S2
s2.sno=200
s2.name="Travis"
s2.marks=77.77
#Display the Object Data of S1
print("Content of s1 Object")
print("\tStudent Number={}".format(s1.sno))
print("\tStudent Name={}".format(s1.name))
print("\tStudent Marks={}".format(s1.marks))
print("-----------------------------------------")
#Display the Object Data of S2
print("Content of s2 Object")
print("\tStudent Number={}".format(s2.sno))
print("\tStudent Name={}".format(s2.name))
print("\tStudent Marks={}".format(s2.marks))
print("-----------------------------------------")




