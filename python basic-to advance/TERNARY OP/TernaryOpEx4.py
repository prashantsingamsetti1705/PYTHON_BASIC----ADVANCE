#Program for Deciding Biggest among them and check for equality
#TernaryOpEx4.py
a=float(input("Enter Value of a:"))
b=float(input("Enter Value of b:"))
bv=a if a>b else b if b>a else "Both Values are Equal"
print("Big({},{})={}".format(a,b,bv))