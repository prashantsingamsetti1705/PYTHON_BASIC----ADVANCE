#Program for Deciding Biggest among Three values and check for equality
#TernaryOpEx5.py
a=float(input("Enter Value of a:"))
b=float(input("Enter Value of b:"))
c=float(input("Enter Value of c:"))
bigv=a if (a>=b) and (a>c) else b if (b>a) and (b>=c) else c if c>=a and c>b else "All Values are equal"
print("Big({},{},{})={}".format(a,b,c,bigv))
