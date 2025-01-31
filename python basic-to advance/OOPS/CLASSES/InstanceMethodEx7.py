#Program for Finding Sum of Two Numbers by using Classes and Objects
#InstanceMethodEx7.py
class Sum:
    def readvalues(self):
        self.a=float(input("Enter First Value:"))
        self.b=float(input("Enter Second Value:"))
    def addvals(self):
        self.c=self.a+self.b
    def dispvals(self):
        print("First Value={}".format(self.a))
        print("Second Value=".format(self.b))
        print("Sum={}".format(self.c))

#Main Program
s=Sum() # Object Creation
s.readvalues() # calling Instance Method
s.addvals()
s.dispvals()