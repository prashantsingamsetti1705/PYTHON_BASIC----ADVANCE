#Program for Cal Div of Two Numbers
#DivEx5.py (Recommended to Write ____________________________  )
#This is the Program written by KVR in 04-11-2024, after 4 Year this code will come for Modification
# In 2028, New Programmer Hinmansu---- Added some new Stmt---There is chance of getting some exception in 2028
try:
	print("Program Execution Started")
	s1=input("Enter First Value:")
	s2=input("Enter Second Value:")
	a=int(s1) #-----------Exception Generated Stmt---ValueError
	b=int(s2) #-----------Exception Generated Stmt---ValueError
	c=a/b    #-----------Exception Generated Stmt---ZeroDivisionError
	s="PYTHON"
	print(s[10])
except ZeroDivisionError:
	print("\tDON'T ENTER ZERO FOR DEN...")
except ValueError:
	print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS")
except IndexError:
	print("Index wrong--Enter Valid Index:")
except : # Default Except Block
	print("ooops Some went wrong with ur Code--Check for exceptions")
else:
	print("------else block------------")
	print("First value=",a)
	print("Second value=",b)
	print("Div=",c)
finally:
	print("-------finally--------------------")
	print("Program Execution Ended")


