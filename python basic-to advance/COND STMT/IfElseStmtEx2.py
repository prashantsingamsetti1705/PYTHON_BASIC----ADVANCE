#Program for Accepting Two Numerical Values and find biggest bu using Simple If statement.
#IfElseStmtEx2.py
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
if(a>b):
    print("max({},{})={}".format(a,b,a))
else:
    if(b>a):
        print("Max({},{})={}".format(a,b,b))
    else:
        print("Both the Values are equal")
    print("I am from if..else--inner")
print("I am from if..else--outer")


