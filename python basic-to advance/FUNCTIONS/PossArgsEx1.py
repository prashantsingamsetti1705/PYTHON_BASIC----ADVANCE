#Program for Demonstrating Positional arguments
#PossArgsEx1.py
def dispstudinfo(sno,sname,marks):
	print("\t{}\t{}\t{}".format(sno,sname,marks))

#Main Program
print("*"*50)
print("\tSNO\tNAME\tMARKS")
print("*"*50)
dispstudinfo(100,"RS",45.67) # Function Call with Pos Args
dispstudinfo(200,"TR",75.67) # Function Call with Pos Args
dispstudinfo(300,"KV",15.67) # Function Call with Pos Args
dispstudinfo(sname="JH",marks=34.56,sno=400) # Function Call with Key word args
dispstudinfo(500,marks=56.78,sname="DR") # Function Call with Pos Args and Key word args
#dispstudinfo(marks=56.78,600,sname="SS") ---SyntaxError: positional argument follows keyword argument
dispstudinfo(marks=56.78,sno=600,sname="SS") # Function Call with Key word args
#dispstudinfo(700,"RD")---TypeError: dispstudinfo() missing 1 required positional argument: 'marks'
print("*"*50)
