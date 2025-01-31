#Program for Accepting Two Numerical Values and find biggest bu using Simple If statement.
#IfElseStmtEx1.py
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
if(a>b):
    print("max({},{})={}".format(a, b, a))
else:
    print("max({},{})={}".format(a, b, b))
print("Program Execution Completed")