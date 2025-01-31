#Program for Demonstrating the Need of Variable Length Arguments
#This Program will Not Execute bcoz PVM Remebers Latest Function Def Only but not previous Def due Its Interpretation Process
#VarArgsEx1.py

def  disp(a,b,c,d,e): # # Function Def-1  with 5 Pos Params
	print(a,b,c,d,e)

def  disp(a,b,c,d): # # Function Def-2  with 4 Pos Params
	print(a,b,c,d)

def  disp(a,b,c): # # Function Def-3  with 3 Pos Params
	print(a,b,c)

def  disp(a,b): # # Function Def-4  with 2 Pos Params
	print(a,b)

def  disp(a): # # Function Def-5  with 1Pos Params
	print(a)

#Main Program
disp(10,20,30,40,50) # Function Call-1 with 5 Pos Args
disp(10,20,30,40) # Function Call-2 with 4 Pos Args
disp(10,20,30) # Function Call-3 with 3 Pos Args
disp(10,20) # Function Call-4 with 2 Pos Args
disp(10) # Function Call-5 with 1 Pos Args