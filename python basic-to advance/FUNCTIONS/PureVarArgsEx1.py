#Program for Demonstrating the Need of Variable Length Arguments
#This Program will  Execute 
#PureVarArgsEx1.py
def  disp(*kvr): # Here *kvr is called Variable Length Parameter and kvr type is <class,tuple>
	print(kvr,type(kvr),len(kvr))



#Main Program
disp(10,20,30,40,50) # Function Call-1 with 5 Pos Args
disp(10,20,30,40) # Function Call-2 with 4 Pos Args
disp(10,20,30) # Function Call-3 with 3 Pos Args
disp(10,20) # Function Call-4 with 2 Pos Args
disp(10) # Function Call-5 with 1 Pos Args
disp()# Function Call-6 with 0 Pos Args
disp([],(),{})
disp(set())
disp(str(),tuple(),set(),list(),dict())
disp("KVR","PYTHON",1.2,2+3j,True)