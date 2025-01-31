#Program for Cal Div of Two Numbers
#DivEx3.py
try:
	print("Program Execution Started")
	s1=input("Enter First Value:")
	s2=input("Enter Second Value:")
	a=int(s1) #-----------Exception Generated Stmt---ValueError
	b=int(s2) #-----------Exception Generated Stmt---ValueError
	c=a/b    #-----------Exception Generated Stmt---ZeroDivisionError
except (ZeroDivisionError,ValueError): # multi exception handling block 
	print("\tDON'T ENTER ZERO FOR DEN...")
	print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS")
else:
	print("------else block------------")
	print("First value=",a)
	print("Second value=",b)
	print("Div=",c)
finally:
	print("-------finally--------------------")
	print("Program Execution Ended")

