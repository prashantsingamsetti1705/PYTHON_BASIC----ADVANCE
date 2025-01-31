#InhProg4.py
class C1:
    def getA(self): # Instance Method
        self.a=float(input("Enter Value of a:")) # Instance Data Member
class C2(C1):
    def getB(self): # Instance Method
        self.b=float(input("Enter Value of b:"))  # Instance Data Member
    def operation(self):
        self.getA() # calling Base Class Method from Derived Class Method
        self.getB()
        self.c=self.a+self.b
        print("Sum({},{})={}".format(self.a,self.b,self.c))
#main program
o2=C2()
o2.operation()

