#Program for cal addition of Two Numbers by using Anonymous Functions
#AnonymousFunEx1.py
def sumop(a,b):
    return a+b
addop=lambda k,v : k+v # Anonymous Function defition

#Main Program
res=sumop(10,20) # Normal Function Call
print("type of sumop=",type(sumop))
print("sum by using normal func=",res)
print("-----------------------------------")
print("Enter Two Values for addition")
a,b=float(input()),float(input())
res1=addop(a,b) # Anonymous  Function Call
print("Type of addop=",type(addop))
print("Sum by using Anonymous Function=",res1)
