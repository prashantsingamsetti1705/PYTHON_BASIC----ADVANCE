#DestEx3.py
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
print("No Longer Interested to use object e1")
time.sleep(5)
e1=None # GC calls Destructor Forcefully
time.sleep(5)
e2=Employee(20,"TR") # Object Creation--makes the PVM to call Parametrized Constructor
print("No Longer Interested to use object e2")
time.sleep(5)
e2=None # GC calls Destructor Forcefully
time.sleep(5)
e3=Employee(30,"JH") # Object Creation--makes the PVM to call Parametrized Constructor
print("No Longer Interested to use object e3")
time.sleep(5)
e3=None # GC calls Destructor Forcefully
print("Program Execution Started")
print("--------------------------------------------------")
