#Program for Understanding globals()
#In this Program we have Different Names for Local and global Variable vals
#globalsFunEx2.py
a=10
b=20
c=30
d=40 # Here a,b,c,d are called Global Variables
def operations():
	x=100
	y=200
	z=300
	k=400 #  Here x,y,z,k are called local Variables
	res=x+y+z+k+a+b+c+d
	print("sum=",res)


#Main Program
operations() # Function Call

