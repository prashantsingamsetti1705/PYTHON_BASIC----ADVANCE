#PolyEx8.py
from math import pi
class Circle:
    def area(self,r): # Original Method
        self.ac=pi*r**2
        print("Area of Circle={}".format(self.ac))
class Square(Circle):
    def area(self,s): # Oeverriden Method
        self.sa=s**2
        print("Area of Square={}".format(self.sa))
        print("--------------------------------")
        super().area(float(input("Enter Radius::")))
class Rect(Square):
    def area(self,L,B): # Overridden Method
        self.ar=L*B
        print("Area of Rect={}".format(self.ar))
        print("--------------------------------")
        super().area(float(input("Enter Side Value of Square:")))

#Main Program
r=Rect()
#accept Length and Breadth from Key Board
L = float(input("Enter Length:"))
B = float(input("Enter Breadth:"))
r.area(L,B)


