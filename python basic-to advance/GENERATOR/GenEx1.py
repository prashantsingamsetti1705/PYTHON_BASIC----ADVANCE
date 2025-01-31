#Program for Demonstrating Geemrators
#GenEx1.py
def kvrrange(x):
	s=0
	while(s<x):
		yield s
		s=s+1


#Main Program
r=kvrrange(6) # Here r is an object of <class, generator>
print(r, type(r)) # <generator object kvrrange at 0x0000020F89915E40> <class 'generator'>
#To get the value from generator object, we use a fucntion called next()
print("------------------------------------------------")
while(True):
	try:
		print(next(r))
	except StopIteration:
		print("------------------------------------------------")
		break