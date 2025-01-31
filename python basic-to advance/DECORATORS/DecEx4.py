#Program for Demonsrating the Multiple Operations like Square, Square Root and Cube by Decorator
#DecEx4.py
def cube(bang):
	def cbvalue():
		n,sqv,sqrtv=bang()
		res=n**3
		return n,sqv,sqrtv,res
	return cbvalue

def squareroot(hyd):
	def sqrtop():
		n,sqv=hyd()
		res=n**0.5
		return n,sqv,res
	return sqrtop


def square(kvr):
	def sqroperation():
		n=kvr()
		res=n**2
		return n,res
	return sqroperation

@cube
@squareroot
@square
def   getval():  # This fun Defined by KVR
	return float(input("Enter Numerical value:"))


#Main Program
n,sqv,sqrtv,cbv=getval() # Normal Function Call
print("Square({})={}".format(n,sqv))
print("Square root({})={}".format(n,sqrtv))
print("Cube({})={}".format(n,cbv))
