#program for Finding Square Root for +Ve Numbers from List of Numerical Values
#DictComprehensionEx2.py
print("Enter List of Values separated by Space:")
ovals=[float(val) for val in input().split() if float(val)>0]
sqrtvals=[float(val)**0.5 for val in ovals]
print("="*50)
print("Given Value\t\tSquareRoot Value")
print("="*50)
for val1,val2 in zip(ovals,sqrtvals):
    print("\t{}\t\t{}".format(val1,round(val2,2)))
print("="*50)