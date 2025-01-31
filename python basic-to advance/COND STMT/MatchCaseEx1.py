#MatchCaseEx1.py
print("="*50)
print("\tArithmetic Operations")
print("="*50)
print("\t1. Addtion")
print("\t2. Substration")
print("\t3. Multiplication")
print("\t4. Division")
print("\t5. Modulo Division")
print("\t6. Exponentiation")
print("\t7. Exit")
print("="*50)
ch=int(input("Enter Ur Choice:"))
match(ch):
    case 1:
        print("Enter Two Values for Addition")
        a,b=float(input()),float(input())
        print("sum({},{})={}".format(a,b,a+b))
    case 2:
        print("Enter Two Values for Substraction")
        a, b = float(input()), float(input())
        print("sub({},{})={}".format(a, b, a - b))
    case 3:
        print("Enter Two Values for Multiplication")
        a, b = float(input()), float(input())
        print("mul({},{})={}".format(a, b, a * b))
    case 4:
        print("Enter Two Values for Division")
        a, b = float(input()), float(input())
        print("Div({},{})={}".format(a, b, a / b))
        print("Floor Div({},{})={}".format(a, b, a // b))
    case 5:
        print("Enter Two Values for Modulo Division")
        a, b = float(input()), float(input())
        print("Mod({},{})={}".format(a, b, a % b))
    case 6:
        a, b = float(input("Enter Base:")), float(input("Enter Power:"))
        print("pow({},{})={}".format(a, b, a ** b))
    case 7:
        print("Thx for Using Program")
    case _: # Default case block
        print("Ur Selection of Operation is wrong--try again")
print("Program execution completed")


