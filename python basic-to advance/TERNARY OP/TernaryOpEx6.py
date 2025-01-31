#Program for Deciding Biggest among Three values and check for equality
#TernaryOpEx6.py
a=float(input("Enter Value of a:"))
b=float(input("Enter Value of b:"))
c=float(input("Enter Value of c:"))
bigv=a if b<=a>c else b if a<b>=c else c if a<=c>b else "All Values are equal"
print("Big({},{},{})={}".format(a,b,c,bigv))