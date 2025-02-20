#Program for generating 1 to N numebrs by using threads
#NumberGenFunEx1.py
import threading,time # Step-1
def numbergenerate(n): # Step-2
	if(n<=0):
		print("{}--> {} is Invalid Input:".format(threading.current_thread().name))
	else:
		for i in range(1,n+1):
			print("{}-->Value of i={}".format(threading.current_thread().name,i))
			time.sleep(0.25)

#Main Program
n=int(input("How Many Numbers u want to Generate:"))
t1=threading.Thread(target=numbergenerate,args=(n,)) # Step-3
t1.start() # Step-4
#now we are woking the subthread
#first we have to import threading
import threading
def sqaure(n):
    print("the square of the value is{}".format(n**2))
def cube(n):
    print("the cube of the value is{}".format(n**3))
#creating the sub objects
t1=threading.Thread(target=sqaure(5))
t2=threading.Thread(target=cube(5))
#the name of sub threads
print("program starting")
print("the thread is {}".format(threading.current_thread().name))
print("the thread is alive",t1.is_alive())
print("the thread is alive",t2.is_alive())
print("the name of the thread",t1.name)
print("the name of the thread",t2.name)
print("-"*100)
t1.start()
print("the thread is alive",t1.is_alive())
t2.start()
print("the thread is alive",t2.is_alive())
print("ending program starting")
print("the thread is {}".format(threading.current_thread().name))
print("-"*100)