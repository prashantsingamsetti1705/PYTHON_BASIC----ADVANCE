#MulTableDemo.py
from MulExcept import ZeroError, NegNumError
from MulTable import table
try:
    n=int(input("Enter a Number for Generating Mul table:"))
    table(n)
except (ZeroError,NegNumError,ValueError):
    print("\tDon't Enter Zero for Mul Table")
    print("\tDon't Enter Neg Number for Mul Table")
    print("\tDon't Enter Alnums,strs and Symbols for Mul Table")
except:
    print("ooops some thing went wrong....")