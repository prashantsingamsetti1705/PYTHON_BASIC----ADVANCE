#Program for Demonstrating the need of global keyword
#GlobalKeywordEx1.py
def  update1():
	a=100
	a=a+1 # Here a is considered by PVM as local Var



#Main Program
a=10 # Global Variable
print("Main Program--Val of a before update()={}".format(a))
update1() # Function Call
print("Main Program--Val of a after update()={}".format(a))