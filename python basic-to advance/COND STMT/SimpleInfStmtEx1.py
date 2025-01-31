#Program for Accepting Two Numerical Values and find biggest bu using Simple If statement.
#SimpleInfStmtEx1.py
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
if a>b:
    print("max({},{})={}".format(a,b,a))
if(b>a):
    print("max({},{})={}".format(a,b,b))
print("Program execution completed")
