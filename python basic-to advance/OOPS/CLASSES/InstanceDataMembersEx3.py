#Program for Storing Sno,name and marks by using Classes and Objects
#InstanceDataMembersEx3.py
class Student:pass

#main program
s1=Student() # Student Object Creation
s2=Student() # Student Object Creation
print("----------------------------------")
#Palce Instance Data Members in S1 by reading values from KBD
s1.sno=int(input("Enter First Student Number:"))
s1.name=input("Enter First Student Name:")
s1.marks=float(input("Enter First Student Marks:"))
print("----------------------------------")
# Here sno,name and marks are called Instance Data Members
#Palce Instance Data Members in S2 by reading values from KBD
s2.sno=int(input("Enter Second Student Number:"))
s2.name=input("Enter Second Student Name:")
s2.marks=float(input("Enter Second Student Marks:"))
print("----------------------------------")
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




