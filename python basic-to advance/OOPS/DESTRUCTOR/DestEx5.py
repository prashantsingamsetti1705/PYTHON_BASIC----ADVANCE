#DestEx5.py
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
print("Program Execution Started")
print("--------------------------------------------------")
