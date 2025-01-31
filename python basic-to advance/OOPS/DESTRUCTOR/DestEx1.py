#DestEx1.py
import time
class Employee:
	def __init__(self,eno,ename):
		print("I am from Parametrized Constructor-Object ID:{}".format(id(self)))
		self.eno=eno
		self.ename=ename
		print("\tEmp Number:{}".format(self.eno))
		print("\tEmp Name:{}".format(self.ename))
		print("--------------------------------------------------")
	def  __del__(self):
		print("GC Calls __del__() for de-allocating the memory space of current object:{}".format(id(self)))

#Main Program
print("Program Execution Started")
print("--------------------------------------------------")
e1=Employee(10,"RS") # Object Creation--makes the PVM to call Parametrized Constructor
e2=Employee(20,"TR") # Object Creation--makes the PVM to call Parametrized Constructor
e3=Employee(30,"JH") # Object Creation--makes the PVM to call Parametrized Constructor
print("Program Execution Started")
print("--------------------------------------------------")
time.sleep(10)
