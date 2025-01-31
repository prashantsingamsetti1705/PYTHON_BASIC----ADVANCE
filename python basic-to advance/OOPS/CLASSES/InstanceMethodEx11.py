#Program for Cal Fctorial of a Number
#InstanceMethodEx10.py
import sys
class Factroial:
    def read(self):
        try:
            self.n=int(input("Enter a Number for Cal Factorial:"))
        except ValueError:
            print("\tDon't enter alnums, strs and symbols")
            sys.exit()
        else:
            res=self.calfact()
            self.disp(res)

    def calfact(self):
        if(self.n<0):
            return "{} is invalid Input".format(self.n)
        else:
            fact = 1
            for i in range(1,self.n+1):
                fact*=i
            else:
                return fact
    def disp(self,res):
        print("Fact({})={}".format(self.n,res))

#Main Program
fo=Factroial()
fo.read()

