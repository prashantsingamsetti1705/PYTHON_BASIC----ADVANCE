#GCEX2.py
import time,sys,gc
class Employee:
	def __init__(self,eno,ename):
		print("I am from Parametrized Constructor-Object ID:{}".format(id(self)))
		self.eno=eno
		self.ename=ename
		print("\tEmp Number:{}".format(self.eno))
		print("\tEmp Name:{}".format(self.ename))
		print("--------------------------------------------------")
	def  __del__(self):
		global memspace
		print("GC Calls __del__() for de-allocating the memory space of current object:{}".format(id(self)))
		memspace=memspace-sys.getsizeof(self)
		print("\tNow Memory space=",memspace)

#Main Program
print("Program Execution Started")
print("Initially, is GC Running=",gc.isenabled())
print("--------------------------------------------------")
e1=Employee(10,"RS") # Object Creation--makes the PVM to call Parametrized Constructor
e2=Employee(20,"TR") # Object Creation--makes the PVM to call Parametrized Constructor
e3=Employee(30,"JH") # Object Creation--makes the PVM to call Parametrized Constructor
#calculate memory space objects of current object
memspace=sys.getsizeof(e1)+sys.getsizeof(e2)+sys.getsizeof(e3)
print("Total Memory space of all objects=",memspace)
gc.disable()
print("Program Execution Ended")
print("Now is GC Running=",gc.isenabled())
print("--------------------------------------------------")
time.sleep(10)
