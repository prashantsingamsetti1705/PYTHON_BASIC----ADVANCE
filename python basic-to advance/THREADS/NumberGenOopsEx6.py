#Program for generating 1 to N numebrs by using threads
#NumberGenOopsEx6.py
import threading,time # Step-1
class Numbers: #Step-2
	def __init__(self,n):
		self.n=n
	def numbergenerate(self): # Step-3
		if(self.n<=0):
			print("{}--> {} is Invalid Input:".format(threading.current_thread().name))
		else:
			for i in range(1,self.n+1):
				print("{}-->Value of i={}".format(threading.current_thread().name,i))
				time.sleep(0.25)

#Main Program
threading.Thread(target=Numbers(int(input("How Many Numbers u want to Generate:"))).numbergenerate).start() # Step-4
