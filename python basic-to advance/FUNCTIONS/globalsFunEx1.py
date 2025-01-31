#Program for Understanding globals()
#globalsFunEx1.py
a=10
b=20 # Here a,b are called global Variables
def operations():
	x=globals() # here x is an object of type <class, dict>
	print("Programmer Defined and Invisible global Variables")
	for gvn,gvv in x.items():
		print("\t{}-->{}".format(gvn,gvv))
	print("--------------------------------------------------------------------------")
	print("Programmer-Defined Global Variables--Way-1")
	print("\tGlobal Var a=",x['a'])
	print("\tGlobal Var b=",x['b'])
	print("--------------------------------------------------------------------------")
	print("Programmer-Defined Global Variables--Way-2")
	print("\tGlobal Var a=",x.get('a'))
	print("\tGlobal Var b=",x.get('b'))
	print("--------------------------------------------------------------------------")
	print("Programmer-Defined Global Variables--Way-3")
	print("\tGlobal Var a=",globals()['a'])
	print("\tGlobal Var b=",globals()['b'])
	print("--------------------------------------------------------------------------")
	print("Programmer-Defined Global Variables--Way-3")
	print("\tGlobal Var a=",globals().get('a'))
	print("\tGlobal Var b=",globals().get('b'))
	print("--------------------------------------------------------------------------")

#Main Program
operations()