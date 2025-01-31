#Program for Factroial  of a number using Recursion
#Recursion3.py
def fact(n):
	if(n<0):
		return "{} Is Invalid Input".format(n)
	else:
		if(n==0):
			return 1
		else:
			return(n*fact(n-1))

#Main Program
n=int(input("Enter n Value:"))
f=fact(n)# Function Call
print("factorial({})={}".format(n,f))