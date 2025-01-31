#Program for Finding Sum of Two Numbers by using Classes and Objects
#InstanceMethodEx6.py
class Sum:pass

#Main Program
s=Sum() # Object Creation
#Read two values for s1 object
s.a=float(input("Enter First Value:"))
s.b=float(input("Enter Second Value:"))
s.c=s.a+s.b
print("sum({},{})={}".format(s.a,s.b,s.c))