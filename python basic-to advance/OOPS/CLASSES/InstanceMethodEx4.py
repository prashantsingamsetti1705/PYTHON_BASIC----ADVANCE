#program for Reading and Displaying the Deatils students by using Classes and Objects
#InstanceMethodEx4.py
class Student:
    def readstuddata(self,objinfo):
        print("----------------------------------")
        print("Enter {} Student Information".format(objinfo))
        self.sno=int(input("\tEnter Student Number:"))
        self.name = input("\tEnter Student Name:")
        self.marks= float(input("\tEnter Student Marks:"))
        print("----------------------------------")
    def dispstuddata(self,objinfo):
        print("----------------------------------")
        print("{} Student Information".format(objinfo))
        print("\tStudent Number:{}".format(self.sno))
        print("\tStudent Name:{}".format(self.name))
        print("\tStudent Marks:{}".format(self.marks))
        print("----------------------------------")
#main Program
s1=Student()
s2=Student()
#read the Student Object Data by using Instance Methods for s1
s1.readstuddata("First") # calling Instance Method
s1.dispstuddata("Second")
#read the Student Object Data by using Instance Methods for s2
s2.readstuddata("Second") # calling Instance Method
s2.dispstuddata("Second")


