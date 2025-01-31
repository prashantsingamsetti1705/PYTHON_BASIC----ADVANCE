#Program for Finding GCD and LCM of Two Numbers
#Recursion4.py
def GCD(m,n):
	if(m%n==0):
		return n
	else:
		return(GCD(n,m%n))

#Main Program
m,n=int(input("Enter m Value:")),int(input("Enter n Value:"))
gcdv=GCD(m,n)
print("GCD({},{})={}".format(m,n,gcdv))
lcmv=(m*n)/gcdv
print("LCM({},{})={}".format(m,n,lcmv))


