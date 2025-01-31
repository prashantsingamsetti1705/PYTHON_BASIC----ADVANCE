#Program for Demonstrating Positional arguments
#PossArgsEx2.py
def dispstudinfo(sno,sname,marks,crs):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

#Main Program
print("*"*50)
print("\tSNO\tNAME\tMARKS\tCOURSE")
print("*"*50)
dispstudinfo(100,"RS",45.67,"PYTHON") # Function Call with Pos Args
dispstudinfo(200,"TR",75.67,"PYTHON") # Function Call with Pos Args
dispstudinfo(300,"KV",15.67,"PYTHON") # Function Call with Pos Args
dispstudinfo(400,"DR",75.97,"PYTHON") # Function Call with Pos Args
dispstudinfo(500,"SS",45.97,"PYTHON") # Function Call with Pos Args
print("*"*50)
