#Program for Understanding the Need of global keyword
#GlobalKwdEx1.py
def increment():
	global a
	a=a+1
	
def updations():
	global a
	a=a*2

#Main Program
a=10 # global var
print("Main Program--Value of a before Increment=",a)
increment() # Function Call
print("Main Program--Value of a after Increment=",a)
updations() # Function call
print("Main Program--Value of a after updations=",a)




#UnboundLocalError: cannot access local variable 'a' where it is not associated with a value