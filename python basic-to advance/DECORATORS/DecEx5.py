#DecEx5.py
def convertupper(bang):
	def upp():
		line,LC=bang()
		return line,LC,line.upper()
	return upp

def convertlower(kvr):
	def low():
		line=kvr()
		return line, line.lower()
	return low


@convertupper
@convertlower
def getline():
	return input("Enter Line of Text:")

#Main Program
line,LC,UC=getline()
print("--------------------------------------------")
print("Given Line:",line)
print('Lower Case:',LC)
print('Upper Case:',UC)
print("--------------------------------------------")
