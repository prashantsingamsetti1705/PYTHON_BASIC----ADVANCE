#Program for Demonsrating the Need of Decorator
#Non-DecEx.py
def   getval():  # This fun Defined by KVR
	return float(input("Enter a Number:"))

def sqaure():						# Sai asking Sir Give me Square of 5
	n=getval()
	res=n**2
	print("square({})={}".format(n,res))

def squareroot():						# Naresh asking Sir give Square Root of 5
	n=getval()
	res=n**0.5
	print("sqrt({})={}".format(n,res))

def cube():						#Deepa asking Sir give Cube of 5
	n=getval()
	res=n**3
	print("cube({})={}".format(n,res))

#Main Program
sqaure()
squareroot()
cube()