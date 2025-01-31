#Program accepting Two Numerical values and Multiply them
#MulEx1.py
print("Enter First Value:")
x=input()
print("Enter Second Value:")
y=input()
#Convert x and y  str values into float type
a=float(x)
b=float(y)
c=a*b
print("-"*50)
print("First Value:{}".format(a))
print("Second Value:{}".format(b))
print("Mul={}".format(c))
print("-----------OR--------------")
print("Mul=%0.2f" %c)
print("-"*50)