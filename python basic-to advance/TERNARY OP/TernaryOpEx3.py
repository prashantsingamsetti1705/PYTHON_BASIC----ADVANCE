#Program for Deciding Whether the Number is +Ve or -Ve or Zero
#TernaryOpEx3.py
n=float(input("Enter any Number:"))
res="ZERO" if n==0 else "+VE" if n>0 else "-VE"
print("{} is {}".format(n,res))
