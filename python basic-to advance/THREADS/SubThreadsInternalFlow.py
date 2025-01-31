#Program for Showing the Internal Flow of Sub Threads and Default Thread
#SubThreadsInternalFlow.py
import threading
def  welcome():
	print("4-welcome()--Executed by:{}".format(threading.current_thread().name))
def  hello():
	print("6-hello()--Executed by:{}".format(threading.current_thread().name))
def  hi():
	print("8-hi()--Executed by:{}".format(threading.current_thread().name))

#main program
print("Line-11:-------------------------------------------------------")
print("Program execution Started by:{}".format(threading.current_thread().name))
print("-------------------------------------------------------")
#Create 3 Sub Threads
t1=threading.Thread(target=welcome) # here t1 is called thread object whose name is Thread-1
t1.name="Rakesh"
t2=threading.Thread(target=hello) # here t2 is called thread object whose name is Thread-2
t2.name="Ramesh"
t3=threading.Thread(target=hi) # here t3 is called thread object whose name is Thread-3
t3.name="Ramu"
#Dsipatch the sub threads
t1.start()
t2.start()
t3.start()
print("-------------------------------------------------------")
print("Program execution Ended by:{}".format(threading.current_thread().name))
print("-------------------------------------------------------")
