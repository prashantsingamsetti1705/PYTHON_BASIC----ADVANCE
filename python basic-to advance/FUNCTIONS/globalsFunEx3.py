#Program for Understanding globals()
#In this Program we have SAME Names for Local and global Variable vals
#globalsFunEx3.py
a=10
b=20
c=30
d=40 # Here a,b,c,d are called Global Variables
def operations():
	a=100
	b=200
	c=300
	d=400 #  Here a,b,c,d are called local Variables
	res=a+b+c+d+globals().get('a') +globals().get('b') +globals()['c']+globals()['d']
	print("sum=",res)

#Main Program
operations() # Function Call

