#Program for adding Two Numbers by using Recursion
#Recursion2.py
def sumbyrecur(m,n):
	if(m==0):
		return n
	else:
		m=m-1
		n=n+1
		return(sumbyrecur(m,n))

#Main Program
m,n=int(input("Enter m Value:")),int(input("Enter n Value:"))
res=sumbyrecur(m,n) # Function Call
print("sum=",res)