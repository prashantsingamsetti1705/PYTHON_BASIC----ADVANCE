#Program accepting Two Numerical values and Multiply them
#MulEx2.py
print("Enter First Value:")
a=float(input())
print("Enter Second Value:")
b=float(input())
#Convert x and y  str values into float type
c=a*b
print("-"*50)
print("First Value:{}".format(a))
print("Second Value:{}".format(b))
print("Mul={}".format(round(c,2)))
print("-----------OR-------------")
print("Mul=%0.2f" %c)
print("-"*50)