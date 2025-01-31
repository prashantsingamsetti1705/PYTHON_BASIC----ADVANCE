#Program for Demonsrating the Multiple Operations like Square, Square Root and Cube by Decorator
#DecEx2.py
def   getval():  # This fun Defined by KVR
	return float(input("Enter Numerical value:"))

def  calculation(kvr):  # Outer Function OR Decorator Function Definition
	def square(): # Inner Function
		n=kvr()
		res=n**2
		return n,res # result of inner Function
	return square # Result of Outer function


#Main Program
res= calculation(getval)()
print("Square({})={}".format(res[0],res[1]))