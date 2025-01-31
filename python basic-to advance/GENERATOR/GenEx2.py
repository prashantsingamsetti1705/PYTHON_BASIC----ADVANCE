#Program for Demonstrating Geemrators
#GenEx2.py
def kvrrange(x):
	s=0
	while(s<x):
		yield s
		s=s+1


#Main Program
r=kvrrange(6) # Here r is an object of <class, generator>
print(r, type(r)) # <generator object kvrrange at 0x0000020F89915E40> <class 'generator'>
#To get the value from generator object, we use a fucntion called next()
print(next(r))
print(next(r))
print("------------------------------------------------")
for val in r:
	print(val)
print("------------------------------------------------")
r1=kvrrange(10)
for val in r1:
	print(val,end="  ")
print("\n------------------------------------------------")