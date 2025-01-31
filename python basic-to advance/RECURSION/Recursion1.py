#Program for Demonstrating Bad Recursion
#Recursion1.py
def fun1(n):
	if(n==0):
		return 
	else:
		print("Good Morning")
		n=n-1
		fun1(n)

#main Program
n=5
fun1(n) # Function Call-----This Program execution gives---RecursionError: maximum recursion depth exceeded