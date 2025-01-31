#SynchBankWithDrawOopsEx.py
import threading,time
class Borower:
	@classmethod
	def getlock(cls):
			#Create an object of Lock Class
			cls.lockobj=threading.Lock()
			Borower.getaccbal()
	@classmethod
	def getaccbal(cls):
			#VM Account Bal
			cls.vmbal=11000
	def __init__(self,camt):
		self.camt=camt
	def  checkclear(self):
		Borower.lockobj.acquire()
		print("----------------------------------------------------------------------------")
		if(self.camt>Borower.vmbal):
			print("\tDear Customer:'{}' , Ur Check of INR:{} Is Bounced-Contact Source".format(threading.current_thread().name,self.camt))
			time.sleep(2)
		else:
			Borower.vmbal=Borower.vmbal-self.camt
			print("\tDear Customer:'{}' , Ur Check of INR:{} Is Cleared".format(threading.current_thread().name,self.camt))
			time.sleep(2)
			print("\tAvailable Balanace in VM Account:{}".format(Borower.vmbal))
		print("----------------------------------------------------------------------------")
		Borower.lockobj.release()


#Main Program
#call Class Level Methods of Borower Class
Borower.getlock()
#Create sub threads
t1=threading.Thread(target=Borower(10000).checkclear)
t1.name="Phanidhra"
t2=threading.Thread(target=Borower(9000).checkclear)
t2.name="Ritwik"
t3=threading.Thread(target=Borower(8000).checkclear)
t3.name="Uma"
t4=threading.Thread(target=Borower(7000).checkclear)
t4.name="Gowthami"
t5=threading.Thread(target=Borower(1000).checkclear,)
t5.name="Rossum"
#Dispatch the sub threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
