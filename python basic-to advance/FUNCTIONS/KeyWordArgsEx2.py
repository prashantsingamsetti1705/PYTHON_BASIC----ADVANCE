#Program for Demonstrating the Keyword Arguments
#KeyWordArgsEx2.py
def  disp(a,b,c,d,city="HYD"):
	print("\t{}\t{}\t{}\t{}\t{}".format(a,b,c,d,city))


#Main Program
print("="*50)
print("\tA\tB\tC\tD\tCITY")
print("="*50)
disp(10,20,30,40) # Function Call with Pos Args
disp(d=40,b=20,a=10,c=30) # Function Call with Keyword Args
disp(c=30,a=10,d=40,b=20) # Function Call with Keyword Args
disp(10,20,d=40,c=30) # Function Call with Pos Args and Keyword Args
#disp(d=40,c=30,10,20)-----SyntaxError: positional argument follows keyword argument
disp(city="AP",d=40,b=20,c=30,a=10)  # Function Call with Keyword Args
print("="*50)