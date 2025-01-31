#Program for Demonstrating the Need of Variable Length Arguments
#PureVarArgsEx4.py
def  calculate(sno,sname,*vals,city="HYD"):  # Here *val is called Variable Length Parameter and vals type is <class,tuple>
	print("----------------------------------------------------")
	print("Student Number:{}".format(sno))
	print("Student Name:{}".format(sname))
	print("Student City:{}".format(city))
	print("----------------------------------------------------")
	if(len(vals)==0):pass
	else:	
		s=0
		for val in vals:
			print("\t{}".format(val))
			s+=val
		print("----------------------------------------------------")
		print("Sum={}".format(s))
		print("----------------------------------------------------")

#Main Program
calculate(100,"RS",10, 20, 30, 40,50)
calculate(200,"TR",10,20,30,40)
calculate(300,"DR",10,20,30)
calculate(400,"DR",10,20)
calculate(500,"SR",10)
calculate(600,"SS",1.2,2.2,3.3,4.4,5.5,6.6,city="AP")
#calculate(600,"SS",city="MUL",1.2,2.2,3.3,4.4,5.5,6.6)---SyntaxError: positional argument follows keyword argument
calculate(700,"KV")