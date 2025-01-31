#InhProg5.py
class GrandParent:
    def getGPP(self):
        self.gpp=float(input("Enter Property Value of Grand Parent:"))
class Parent(GrandParent):
    def getPP(self):
        self.pp = float(input("Enter Property Value of Parent:"))
class Child(Parent):
    def getCP(self):
        self.cp=float(input("Enter Property Value of Child:"))
    def totalprop(self):
        self.totp=self.gpp+self.pp+self.cp
        print("-"*50)
        print("Grand Parent Property={}".format(self.gpp))
        print("Parent Property={}".format(self.pp))
        print("Child Property={}".format(self.cp))
        print("TOTAL PROPERTY={}".format(self.totp))
        print("-" * 50)

#Main Program
co=Child()
co.getCP()
co.getPP()
co.getGPP()
co.totalprop()
