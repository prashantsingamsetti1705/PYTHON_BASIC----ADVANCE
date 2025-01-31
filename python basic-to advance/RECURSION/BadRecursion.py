#Program for Demonstrating Bad Recursion
#BadRecursion.py
def fun1():
	print("Hello Recursion")
	fun1()

#main Program
fun1() # Function Call-------This Program execution gives---RecursionError: maximum recursion depth exceeded