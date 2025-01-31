#program for Finding Square Root for +Ve Numbers from List of Numerical Values
#DictComprehensionEx2.py
print("Enter List of Values separated by comma:")
sqrtvals={float(val):round(float(val)**0.5,2)  for val in input().split(",")  if float(val)>0 }
print("="*50)
print("Given Value\t\tSquareRoot Value")
print("="*50)
for val1,val2 in sqrtvals.items():
    print("\t{}\t\t{}".format(val1,val2))
print("="*50)