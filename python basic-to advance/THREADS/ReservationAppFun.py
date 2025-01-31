#ReservationAppFun.py
import threading,time
def reservation(nos):
	lk.acquire()
	print("----------------------------------------------------------------------------")
	global totseats
	if(nos>totseats):
		print("\tDear Passenger:'{}', {} Seats are not Available-better luck next time".format(threading.current_thread().name,nos))
		time.sleep(2)
	else:
		totseats=totseats-nos
		print("\tDear Passenger:'{}', {} Seats are ResevedHpy Jrny".format(threading.current_thread().name,nos))
		time.sleep(2)
		print("\tAvailable Seats=",totseats)
		if(totseats==0):
			print("\tBUS IS FULL")
	print("----------------------------------------------------------------------------")
	lk.release()


#Main Program
#Create an object of Lock
lk=threading.Lock()
#Number of Seats in BUs
totseats=12
#Create Multiple Passenger Threads
t1=threading.Thread(target=reservation,args=(4,))
t1.name="Pavan"
t2=threading.Thread(target=reservation,args=(8,))
t2.name="Hasshit"
t3=threading.Thread(target=reservation,args=(3,))
t3.name="Younis"
t4=threading.Thread(target=reservation,args=(6,))
t4.name="Sai"
#dispatch all the threads
t1.start()
t2.start()
t3.start()
t4.start()

