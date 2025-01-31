#PolyEx7.py
from math import pi
class Circle:
    def __init__(self): # Original Method
        self.r=float(input("Enter Radius:"))
        self.ac=pi*self.r**2
        print("Area of Circle={}".format(self.ac))
class Square:
    def __init__(self): # Original Method
        self.s=float(input("Enter Side Value of Square:"))
        self.sa=self.s**2
        print("Area of Square={}".format(self.sa))
class Rect(Circle,Square):
    def __init__(self): # Overridden Method
        self.L = float(input("Enter Length:"))
        self.B = float(input("Enter Breadth:"))
        self.ar=self.L*self.B
        print("Area of Rect={}".format(self.ar))
        print("----------------------------------")
        super().__init__()
        print("----------------------------------")
        Square.__init__(self)
#Main Program
r=Rect()



