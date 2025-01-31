#program for Reading and Displaying the Deatils students by using Classes and Objects
#InstanceMethodEx2.py
class Student:
    def readstuddata(self,objinfo):
        print("----------------------------------")
        print("Enter {} Student Information".format(objinfo))
        self.sno=int(input("\tEnter Student Number:"))
        self.name = input("\tEnter Student Name:")
        self.marks= float(input("\tEnter Student Marks:"))
        print("----------------------------------")

#main Program
s1=Student()
s2=Student()
#read the Student Object Data by using Instance Methods
s1.readstuddata("First") # calling Instance Method
s2.readstuddata("Second") # calling Instance Method
#display the objects data by using Instance Methods
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


