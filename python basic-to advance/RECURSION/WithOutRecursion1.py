#Program for adding Two Numbers by using Loops
#WithOutRecursion1.py
def sumbyrecur(m,n):
		if(m==0):
			return n
		elif(n==0):
			return m
		elif(m!=n):
			s=0
			while(m!=n):
				m=m-1
				n=n+1
				if(m==0):
					s=n
					break
			return s	

#Main Program
m,n=int(input("Enter m Value:")),int(input("Enter n Value:"))
res=sumbyrecur(m,n) # Function Call
print("sum=",res)