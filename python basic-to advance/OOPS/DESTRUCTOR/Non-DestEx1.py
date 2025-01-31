#Non-DestEx1.py
class Employee:
	def __init__(self,eno,ename):
		print("I am from Parametrized Constructor:")
		self.eno=eno
		self.ename=ename
		print("\tEmp Number:{}".format(self.eno))
		print("\tEmp Name:{}".format(self.ename))
		print("--------------------------------------------------")

#Main Program
print("Program Execution Started")
print("--------------------------------------------------")
e1=Employee(10,"RS") # Object Creation--makes the PVM to call Parametrized Constructor
e2=Employee(20,"TR") # Object Creation--makes the PVM to call Parametrized Constructor
e3=Employee(30,"JH") # Object Creation--makes the PVM to call Parametrized Constructor
print("Program Execution Started")
print("--------------------------------------------------")
