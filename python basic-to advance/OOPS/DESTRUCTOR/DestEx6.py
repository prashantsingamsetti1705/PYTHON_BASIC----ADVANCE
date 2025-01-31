#DestEx6.py
import time
class Employee:
	def __init__(self,eno,ename):
		print("I am from Parametrized Constructor:")
		self.eno=eno
		self.ename=ename
		print("\tEmp Number:{}".format(self.eno))
		print("\tEmp Name:{}".format(self.ename))
		print("--------------------------------------------------")
	def  __del__(self):
		print("GC Calls __del__() for de-allocating the memory space of current object:")

#Main Program
print("Program Execution Started")
print("--------------------------------------------------")
e1=Employee(10,"RS") # Object Creation--makes the PVM to call Parametrized Constructor
e2=e1 # Deep Copy
e3=e1  # Deep Copy
print("No Longer Interested to use object e1")
time.sleep(5)
e1=None # GC will not calls Destructor Forcefully bcoz still e2 and e3 points object memory space
print("No Longer Interested to use object e2")
time.sleep(5)
del e2 # GC will not calls Destructor Forcefully bcoz still  e3 points object memory space
print("No Longer Interested to use object e3")
time.sleep(5)
del e3 # GC calls Destructor Forcefully bcoz  No objects  points object memory space
print("Program Execution Started")
print("--------------------------------------------------")
