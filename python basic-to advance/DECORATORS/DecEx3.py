#Program for Demonsrating the Multiple Operations like Square, Square Root and Cube by Decorator
#DecEx3.py

def square(kvr):
	def sqroperation():
		n=kvr()
		res=n**2
		return n,res
	return sqroperation

@square
def   getval():  # This fun Defined by KVR
	return float(input("Enter Numerical value:"))


#Main Program
n,res=getval() # Normal Function Call
print("Square({})={}".format(n,res))
