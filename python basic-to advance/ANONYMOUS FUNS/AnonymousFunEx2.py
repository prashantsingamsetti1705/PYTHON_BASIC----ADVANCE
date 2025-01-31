#Program for performing Different types of Arithmetic Operations by using Anonymous Function
#AnonymousFunEx2.py
from operator import floordiv


def arithmenu():
    print("=" * 50)
    print("\tArithmetic Operations")
    print("=" * 50)
    print("\t1. Addtion")
    print("\t2. Substration")
    print("\t3. Multiplication")
    print("\t4. Division")
    print("\t5. Floor Division")
    print("\t6. Modulo Division")
    print("\t7. Exponentiation")
    print("\t8. Exit")
    print("=" * 50)
#Anonymous Functions Definition
addop=lambda k,v: k+v
subop=lambda k,v: k-v
mulop=lambda a,b: a*b
divop=lambda k,v: k/v
floordivop=lambda k,v: k//v
modop=lambda k,v:k%v
powop=lambda k,v: k**v


#Main Program
while(True):
    arithmenu()
    ch=int(input("Enter Ur Choice:"))
    match(ch):
        case 1:
            print("Enter Two Values for addition")
            a, b = float(input()), float(input())
            res1 = addop(a, b)  # Anonymous  Function Call
            print("\tsum({},{})={}".format(a,b,res1))
        case 2:
            print("Enter Two Values for Substraction")
            a, b = float(input()), float(input())
            res1 = subop(a, b)  # Anonymous  Function Call
            print("\tsub({},{})={}".format(a, b, res1))
        case 3:
            print("Enter Two Values for Multiplication")
            a, b = float(input()), float(input())
            res1 = mulop(a, b)  # Anonymous  Function Call
            print("\tmul({},{})={}".format(a, b, res1))
        case 4:
            print("Enter Two Values for Normal Div")
            a, b = float(input()), float(input())
            res1 = divop(a, b)  # Anonymous  Function Call
            print("\tdiv({},{})={}".format(a, b, res1))
        case 5:
            print("Enter Two Values for Floor Div")
            a, b = float(input()), float(input())
            res1 = floordiv(a, b)  # Anonymous  Function Call
            print("\tsum({},{})={}".format(a, b, res1))
        case 6:
            print("Enter Two Values for Mod Div")
            a, b = float(input()), float(input())
            res1 = modop(a, b)  # Anonymous  Function Call
            print("\tmod({},{})={}".format(a, b, res1))
        case 7:
            a, b = float(input("Enter Base:")), float(input("Enter Power:"))
            res1 = powop(a, b)  # Anonymous  Function Call
            print("\tpow({},{})={}".format(a, b, res1))

        case 8:
            print("Thx for using this program")
            break
        case _:
            print("Ur Selection of Operation is wrong-try again")