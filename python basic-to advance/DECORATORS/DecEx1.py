#Program for Demonsrating the Multiple Operations like Square, Square Root and Cube by Decorator
#DecEx1.py
def   getval():  # This fun Defined by KVR
	return float(input("Enter Numerical value:"))

def  calculation(kvr):  # Outer Function OR Decorator Function Definition
	def square(): # Inner Function
		n=kvr()
		res=n**2
		return n,res # result of inner Function
	return square # Result of Outer function


#Main Program
result=calculation(getval) # A Function Call Taking Normal Fun Name as argument--Called Decorator
n,sqv=result()
print("Square({})={}".format(n,sqv))