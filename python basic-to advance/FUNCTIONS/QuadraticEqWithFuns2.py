#Program for calculating Roots of Quadratic Equation
#QuadraticEqWithFuns.py
def getvalues():
    a,b,c=int(input("Enter Value of a:")),int(input("Enter Value of b:")),int(input("Enter Value of c:"))
    rootscal(a,b,c) # One Function is calling another Function

def rootscal(a,b,c):
    if(a==0):
        print("Invalid Values for Quadratic Equation:")
    else:
        D=(b**2-4*a*c)
        print("--------------------------------------")
        if(D>0):
            print("Roots are Real and Distinct")
            r1=(-b+D**0.5)/(2*a)
            r2=(-b-D**0.5)/(2*a)
            print("Root1={}".format(r1))
            print("Root2={}".format(r2))
        elif(D==0):
            print("Roots are Real and Equal")
            r1 = -b  / (2 * a)
            r2 = -b  / (2 * a)
            print("Root1={}".format(r1))
            print("Root2={}".format(r2))
        else:
            print("Roots are Real and Imaginary")
            r1 = (-b + D ** 0.5) / (2 * a)
            r2 = (-b - D ** 0.5) / (2 * a)
            print("Root1={}".format(r1))
            print("Root2={}".format(r2))
        print("--------------------------------------")
#Main Program
getvalues()
