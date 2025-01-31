#Program for Understanding the Need of global keyword
#GlobalKwdEx2.py
def increment():
	global a,b
	a=a+1
	b=b+1

def updations():
	global a,b
	a=a*2
	b=b*2

def accessvals():
	#No Need to write global keyword at this point of time bcoz we are just accessing and modified val kept local var but not in global var
	c=a+2
	d=b+2
	print("\tLocal Vals c={} and d={}".format(c,d))

#Main Program
a=10 # global var
b=20 # global var
print("Main Program--a={} and b={} before incrment".format(a,b))  # a=10  b=20
increment() # Function Call
print("Main Program--a={} and b={} after incrment".format(a,b))  # a=11  b=21
updations() # Function call
print("Main Program--a={} and b={} after updations".format(a,b)) # a=22  b=42
accessvals()
print("Main Program--a={} and b={} after accessvals()".format(a,b)) # a=22  b=42




#UnboundLocalError: cannot access local variable 'a' where it is not associated with a value