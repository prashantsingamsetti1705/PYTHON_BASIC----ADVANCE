#PolyExStrong15.py
from math import pi
class Circle:
    def __init__(self, r):  # Original Constructor
        self.ac = pi * r ** 2
        print("Area of Circle={}".format(round(self.ac, 2)))
class Square(Circle):
    def __init__(self, s):  # Overriden Constructor
        self.sa = s ** 2
        print("Area of Square={}".format(self.sa))
class Rect(Square):
    def __init__(self,s=0):pass

    def area(self, L, B):  # Method Name
        self.ar = L * B
        print("Area of Rect={}".format(self.ar))
        print("--------------------------------")
        super().__init__(float(input("Enter Side Value of Square:")))
        print("--------------------------------")
        Circle.__init__(self,float(input("Enter Radius:")))
#main Program
r = Rect() # Object Creation--PVM Calls Default Cont of Rect Class
L = float(input("Enter Length:"))
B = float(input("Enter Breadth:"))
r.area(L,B)