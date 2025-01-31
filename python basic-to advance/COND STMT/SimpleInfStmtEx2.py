#Program for Accepting Two Numerical Values and find biggest bu using Simple If statement.
#SimpleInfStmtEx1.py
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
if a>b:  # Simple IF Statement
    print("max({},{})={}".format(a,b,a))
if(b>a):   # Simple IF Statement
    print("max({},{})={}".format(a,b,b))
if(a==b):    # Simple IF Statement
    print("Both Values are equal")
print("Program execution completed")
