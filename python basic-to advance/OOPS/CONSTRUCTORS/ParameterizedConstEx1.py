#ParameterizedConstEx1.py
class Test:
    def __init__(self,k,v):
        print("I am from Parameterized Constructor")
        self.a=k
        self.b=v
        print("\tVal of a={}".format(self.a))
        print("\tVal of b={}".format(self.b))
        print("-------------------------------")

#Main Program
#I want Create three objects of test class and
# Initlize all 3 objects with Different values
t1=Test(10,20) # Object Creation--Makes the PVM to call Parameterized Constructor
t2=Test(100,200) # Object Creation--Makes the PVM to call Parameterized Constructor
t3=Test(1000,2000) # Object Creation--Makes the PVM to call Parameterized Constructor