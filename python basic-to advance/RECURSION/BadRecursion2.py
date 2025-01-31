#Program for Demonstrating Bad Recursion
#BadRecursion2.py
def fun1():
	print("Calling Fun2()")
	fun2() # calling fun2()

def fun2():
	print("Calling Fun1()")
	fun1() # calling fun1()

#main Program
fun1() # Function Call-------This Program execution gives---RecursionError: maximum recursion depth exceeded