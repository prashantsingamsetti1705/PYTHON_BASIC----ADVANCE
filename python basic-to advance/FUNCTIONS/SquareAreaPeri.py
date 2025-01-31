#Program for calculating area and perimeter of Square
#SquareAreaPeri.py
def squarearea():
    s=float(input("Enter Value of Side for Cal Area of Square:"))
    sa=s**2
    print("Area of Square={}".format(sa))

def squareperi():
    s = float(input("Enter Value of Side for Cal Perimeter of Square:"))
    ps = 4*s
    print("Perimeter of Square={}".format(ps))

#Main Program
squareperi()
squarearea()