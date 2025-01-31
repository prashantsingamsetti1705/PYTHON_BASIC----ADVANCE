#PolyEx9.py
from math import pi
class Circle:
    def area(self,r): # Original Method
        self.ac=pi*r**2
        print("Area of Circle={}".format(round(self.ac,2)))
class Square(Circle):
    def area(self,s): # Oeverriden Method
        self.sa=s**2
        print("Area of Square={}".format(self.sa))

class Rect(Square):
    def area(self,L,B): # Overridden Method
        self.ar=L*B
        print("Area of Rect={}".format(self.ar))
        print("--------------------------------")
        Square.area(self,float(input("Enter Side Value of Square:")))
        print("--------------------------------")
        Circle.area(self,float(input("Enter Radius::")))


#Main Program
r=Rect()
#accept Length and Breadth from Key Board
L = float(input("Enter Length:"))
B = float(input("Enter Breadth:"))
r.area(L,B)


