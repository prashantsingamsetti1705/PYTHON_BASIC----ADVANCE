#SynchBankWithDrawFunEx.py
import threading,time
def  checkclear(camt):
	lockobj.acquire()
	global vmbal
	print("----------------------------------------------------------------------------")
	if(camt>vmbal):
		print("\tDear Customer:'{}' , Ur Check of INR:{} Is Bounced-Contact Source".format(threading.current_thread().name,camt))
		time.sleep(2)
	else:
		vmbal=vmbal-camt
		print("\tDear Customer:'{}' , Ur Check of INR:{} Is Cleared".format(threading.current_thread().name,camt))
		time.sleep(2)
		print("\tAvailable Balanace in VM Account:{}".format(vmbal))
	print("----------------------------------------------------------------------------")
	lockobj.release()


#Main Program
#VM Account Bal
vmbal=11000
#Create an object of Lock Class
lockobj=threading.Lock()
#Create sub threads
t1=threading.Thread(target=checkclear,args=(10000,))
t1.name="Phanidhra"
t2=threading.Thread(target=checkclear,args=(9000,))
t2.name="Ritwik"
t3=threading.Thread(target=checkclear,args=(8000,))
t3.name="Uma"
t4=threading.Thread(target=checkclear,args=(7000,))
t4.name="Gowthami"
t5=threading.Thread(target=checkclear,args=(1000,))
t5.name="Rossum"
#Dispatch the sub threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
