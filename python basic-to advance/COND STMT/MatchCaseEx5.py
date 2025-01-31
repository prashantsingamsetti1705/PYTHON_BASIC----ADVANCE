#MatchCaseEx5.py
import sys
s="""=================================================
				Area of Different Figures
=================================================
				R. Rectangle
				T. Triangle
				S. Square
				C. Circle
				E. Exit
================================================="""
print(s)
ch=input("Enter Ur Choice:")
match(ch.upper()):
    case "R":
        L,B=float(input("Enter Length:")),float(input("Enter Breadth:"))
        ar=L*B
        print("Area of Rect={}".format(ar))
    case "T":
        B, H = float(input("Enter Base:")), float(input("Enter Height:"))
        at=(1/2)*B*H
        print("Area of Triangle:{}".format(at))
        print("--------------OR--------------------------")
        a,b,c=float(input("Enter Side1:")),float(input("Enter Side2:")),float(input("Enter Side3:"))
        s=(a+b+c)/2
        ats=(s*(s-a)*(s-b)*(s-c))**0.5
        print("Area of Triangle:{}".format(ats))
    case "S":
        s1 = float(input("Enter Side:"))
        sa = s1*s1
        print("Area of Square={}".format(sa))
    case "C":
        r = float(input("Enter Radius:"))
        ca = 3.14*r**2
        print("Area of Square={}".format(ca))
    case "E":
        print("thx for using Program")
        sys.exit()
    case _:
        print("Ur Selection of Operation is Wrong--try again")
