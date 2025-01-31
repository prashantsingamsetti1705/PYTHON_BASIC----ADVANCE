#Program for Demonstrating the Elimination of Dead Lock with Synchronization.
#SynchOopsEx1.py
import threading,time
class Table:
	def MulTable(self,n):
		#Get the lock
		L.acquire() # Step-2
		if(n<=0):
			print("{}--> {} is Invalid Input".format(threading.current_thread().name,n))
		else:
			print("-"*50)
			print("Mul Table for:{}".format(n))
			print("-"*50)
			for i in range(1,11):
				print("\t{}---->{} x {}={}".format(threading.current_thread().name,n,i,n*i))
				time.sleep(0.125)
			
		print("-------------------------------------------------------------")
		#release the lock
		L.release() # Step-3

#Main Program
#Create an object of Lock class of threading
L=threading.Lock() # Step-1
#Create sub threads
t1=threading.Thread(target=Table().MulTable,args=(19,))
t2=threading.Thread(target=Table().MulTable,args=(17,))
t3=threading.Thread(target=Table().MulTable,args=(-9,))
t4=threading.Thread(target=Table().MulTable,args=(14,))
#dispatch the sub threads
t1.start()
t2.start()
t3.start()
t4.start()
