#Program for Cal Div of Two Numbers
#DivEx1.py
print("Program Execution Started")
s1=input("Enter First Value:")
s2=input("Enter Second Value:")
print("First value=",s1)
print("Second value=",s2)
a=int(s1) #-----------Exception Generated Stmt---ValueError
b=int(s2) #-----------Exception Generated Stmt---ValueError
c=a/b    #-----------Exception Generated Stmt---ZeroDivisionError
print("Div=",c)
print("Program Execution Ended")