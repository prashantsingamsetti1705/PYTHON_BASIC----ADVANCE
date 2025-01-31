#Program for adding of Two  Numbers by using Functions
#INPUT     : Taking from Function Call
#PROCESS   : Done inside of Function Body
#RESULT    : Giving Back to Function Call
#ApprochEx1.py
def addop(a,b): # Here a and b are called Formal Parameters
    c=a+b # Here c is called Local Variable
    return c

#Main Program
x=float(input("Enter First Value:"))
y=float(input("Enter Second Value:"))
z=addop(x,y) # function call
print("sum({},{})={}".format(x,y,z))
print("---------------------------------------")
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
c=addop(a,b) # function call
print("sum({},{})={}".format(a,b,c))
