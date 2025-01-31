#InhProg7.py
class GrandParent:
    def getGPP(self):
        self.p=float(input("Enter Property Value of Grand Parent:"))
        return self.p
class Parent:
    def getPP(self):
        self.p = float(input("Enter Property Value of Parent:"))
        return self.p
class Child(Parent,GrandParent):
    def getCP(self):
        self.p=float(input("Enter Property Value of Child:"))
        return self.p
    def totalprop(self):
        x=self.getGPP()
        y=self.getPP()
        z=self.getCP()
        tp=x+y+z
        print("-"*50)
        print("Grand Parent Property={}".format(x))
        print("Parent Property={}".format(y))
        print("Child Property={}".format(z))
        print("TOTAL PROPERTY={}".format(tp))
        print("-" * 50)

#Main Program
co=Child()
co.totalprop()