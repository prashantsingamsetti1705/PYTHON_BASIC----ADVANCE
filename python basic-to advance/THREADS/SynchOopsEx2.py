#Program for Demonstrating the Elimination of Dead Lock with Synchronization.
#SynchOopsEx2.py
import threading,time
class Table:
	def __init__(self,n):
			self.n=n
	def MulTable(self):
		#Get the lock
		L.acquire() # Step-2
		if(self.n<=0):
			print("{}--> {} is Invalid Input".format(threading.current_thread().name,self.n))
		else:
			print("-"*50)
			print("Mul Table for:{}".format(self.n))
			print("-"*50)
			for i in range(1,11):
				print("\t{}---->{} x {}={}".format(threading.current_thread().name,self.n,i,self.n*i))
				time.sleep(0.125)
			
		print("-------------------------------------------------------------")
		#release the lock
		L.release() # Step-3

#Main Program
#Create an object of Lock class of threading
L=threading.Lock() # Step-1
#Create sub threads
t1=threading.Thread(target=Table(19).MulTable)
t2=threading.Thread(target=Table(17).MulTable)
t3=threading.Thread(target=Table(-9).MulTable)
t4=threading.Thread(target=Table(14).MulTable)
#dispatch the sub threads
t1.start()
t2.start()
t3.start()
t4.start()
