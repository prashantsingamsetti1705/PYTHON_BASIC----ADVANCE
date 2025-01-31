#DivDemo.py<---Main Program
from Division import divop
from NumberDivisionError import NumberDivisionError
try:
    a=int(input("Enter First Value:"))
    b=int(input("Enter Second Value:"))
    try:
        res=divop(a,b) # Function Call----gives either Result OR exception
    except NumberDivisionError:
        print("\tDON'T ENTER ZERO FOR DEN.....")
    else:
        print("Div({},{})={}".format(a,b,res))
except ValueError:
    print("\tDon't enter alnums,strs and symbols")
finally:
    print("I am from finally block-outer try")

#Phase-3: Handling of the exceptions.