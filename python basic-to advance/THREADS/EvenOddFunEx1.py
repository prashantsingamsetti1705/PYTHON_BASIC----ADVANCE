#Program for Generating Odd and Even threads by using Multiple Threads
#EvenOddFunEx1.py
import threading,time
def odd(n):
	if(n<=0):
		print("{}---> {} is Invalid Input".format(threading.current_thread().name,n))
	else:
		for i in range(1,n+1,2):
			print("{}--->Odd: {} ".format(threading.current_thread().name,i))
			time.sleep(1)

def even(n):
	if(n<=0):
		print("{}---> {} is Invalid Input".format(threading.current_thread().name,n))
	else:
		for i in range(2,n+1,2):
			print("{}--->Even: {} ".format(threading.current_thread().name,i))
			time.sleep(1)

#Main Program
print("Program Execution Started by:{}".format(threading.current_thread().name))
#Create Two Sub Threads for Perform Two Operations
t1=threading.Thread(target=odd,args=(10,))
t2=threading.Thread(target=even,args=(10,))
print("Number Threads which are running before start={}".format(threading.active_count()) )# 1
#Dispatch the sub threads
t1.start()
t2.start()
print("Number Threads which are running after start={}".format(threading.active_count()) )# 3
#Join the sub threads
t1.join()
t2.join()
print("Number Threads which are running after joining={}".format(threading.active_count()) )# 1
print("Program Execution Ended by:{}".format(threading.current_thread().name))
