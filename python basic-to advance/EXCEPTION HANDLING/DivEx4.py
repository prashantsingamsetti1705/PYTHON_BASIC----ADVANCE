#Program for Cal Div of Two Numbers
#DivEx4.py (Only writing Default Block is Not Recommended )
try:
	print("Program Execution Started")
	s1=input("Enter First Value:")
	s2=input("Enter Second Value:")
	a=int(s1) #-----------Exception Generated Stmt---ValueError
	b=int(s2) #-----------Exception Generated Stmt---ValueError
	c=a/b    #-----------Exception Generated Stmt---ZeroDivisionError
except: # Deafult Except Block
	print("Oooops Some Thing went wrong!!!!")
else:
	print("------else block------------")
	print("First value=",a)
	print("Second value=",b)
	print("Div=",c)
finally:
	print("-------finally--------------------")
	print("Program Execution Ended")


