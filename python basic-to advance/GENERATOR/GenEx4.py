#GenEx4.py
def getcrses():
	yield "PYTHON"
	yield "Django"
	yield "HTML"
	yield "C"
	yield "DSA"
	yield 1.2

#Main Program
gs=getcrses()
print("type of gs=",type(gs))
print(next(gs))
print(next(gs))
print(next(gs))
print(next(gs))
print(next(gs))
print(next(gs))
