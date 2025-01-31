#Program for adding of Two  Numbers by using Functions
#INPUT     : Taking from Function Call
#PROCESS   : Done inside of Function Body
#RESULT    : Inside the Function Body
def addop(a,b):
    c=a+b
    print("sum({},{})={}".format(a,b,c))

#Main Program
x=float(input("Enter First Value:"))
y=float(input("Enter Second Value:"))
addop(x,y) # Function Call
