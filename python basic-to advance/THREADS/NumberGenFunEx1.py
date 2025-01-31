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
