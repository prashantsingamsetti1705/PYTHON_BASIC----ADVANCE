#Program for Generating Odd and Even threads by using Multiple Threads
#EvenOddOopEx2.py
import threading,time
class OddNumbers:
	def odd(self,n):
		if(n<=0):
			print("{}---> {} is Invalid Input".format(threading.current_thread().name,n))
		else:
			for i in range(1,n+1,2):
				print("{}--->Odd: {} ".format(threading.current_thread().name,i))
				time.sleep(1)
class EvenNumbers:
	def even(self,n):
		if(n<=0):
			print("{}---> {} is Invalid Input".format(threading.current_thread().name,n))
		else:
			for i in range(2,n+1,2):
				print("{}--->Even: {} ".format(threading.current_thread().name,i))
				time.sleep(1)

#Main Program
print("Program Execution Started by:{}".format(threading.current_thread().name))
#Create Two Sub Threads for Perform Two Operations
t1=threading.Thread(target=OddNumbers().odd,args=(int(input("Enter How Many Odd Numbers u want to generate:")),))
t2=threading.Thread(target=EvenNumbers().even,args=(int(input("Enter How Many Even Numbers u want to generate:")),))
#Dispatch the sub threads
t1.start()
t2.start()
#Join the sub threads
t1.join()
t2.join()
print("Number Threads which are running after joining={}".format(threading.active_count()) )# 1
print("Program Execution Ended by:{}".format(threading.current_thread().name))
