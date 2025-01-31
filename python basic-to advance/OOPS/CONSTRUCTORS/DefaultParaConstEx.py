#DefaultParaConstEx.py
class Test:
    def __init__(self,a=1,b=2):
        print("i am from Default / Parameterized Constructor")
        self.a=a
        self.b=b
        print("\tVal of a={}".format(self.a))
        print("\tVal of b={}".format(self.b))
        print("-------------------------------")

#Main Program
#I want Create mutiple objects of test class and
# Initlize all 1 objects with same values 1 and 2
# and other Object with Different Values
t1=Test() # Object Creation--Makes the PVM to call Default Constructor
t2=Test(10,20)# Object Creation--Makes the PVM to call Parameterized Constructor
t3=Test(100,200)# Object Creation--Makes the PVM to call Parameterized Constructor
t4=Test(1000)# Object Creation--Makes the PVM to call Parameterized Constructor
t5=Test(b=1000)# Object Creation--Makes the PVM to call Parameterized Constructor
t6=Test(b=150,a=140)# Object Creation--Makes the PVM to call Parameterized Constructor