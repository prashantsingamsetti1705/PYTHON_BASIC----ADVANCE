#DefaultConsEx1.py
class Test:
    def __init__(self):
        print("i am from Default Constructor")
        self.a=1
        self.b=2
        print("\tVal of a={}".format(self.a))
        print("\tVal of b={}".format(self.b))
        print("-------------------------------")

#Main Program
#I want Create three objects of test class and
# Initlize all 3 objects with same values 1 and 2
t1=Test() # Object Creation--Makes the PVM to call Default Constructor
t2=Test() # Object Creation--Makes the PVM to call Default Constructor
t3=Test() # Object Creation--Makes the PVM to call Default Constructor