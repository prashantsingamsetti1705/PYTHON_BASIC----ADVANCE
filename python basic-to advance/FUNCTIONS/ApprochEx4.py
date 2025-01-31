#Program for adding of Two  Numbers by using Functions
#INPUT     : Inside the Function Body
#PROCESS   : Inside the Function Body
#RESULT    : Giving Back to Function Call
#ApprochEx4.py
def addop():
    # Take the Input
    a = float(input("Enter First Value:"))
    b = float(input("Enter Second Value:"))
    # Processing
    c = a + b
    #Give the Result Back to Function Call
    return a,b,c # here return not returns Single Value But also returns More than one value
#Main Program
a,b,c=addop() # Function Call with Multi Line assigment
print("sum({},{})={}".format(a,b,c))
print("---------------OR---------------------")
res=addop() # Function Call with Single Line assigment
#here res is an object of <class, tuple>
print("sum({},{})={}".format(res[0],res[1],res[2]))
print("-----------OR----------------")
print("sum({},{})={}".format(res[-3],res[-2],res[-1]))