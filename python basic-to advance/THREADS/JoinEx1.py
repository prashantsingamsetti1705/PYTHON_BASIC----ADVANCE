#Program for Demonstrating the need of join() of Thread class
#JoinEx1.py
import threading,time
def   welcome(val):
	print("\t\t{}-->Hi {}, Good Morning".format(threading.current_thread().name,val))
	time.sleep(10)
	print("\t\t{} coming out from sleep".format(threading.current_thread().name))


#Main Program
print("Program execution started  by :{}".format(threading.current_thread().name))
t1=threading.Thread(target=welcome,args=("Rossum",))
print("Execution Status of Sub Thread t1 before start()=",t1.is_alive())
#dispatch the sub thread t1
t1.start()
print("Execution Status of Sub Thread t1 after start()=",t1.is_alive())
#Make the MainThread to wait until Sub Threads joins with MainThread
t1.join()
print("Execution Status of Sub Thread t1 after join()=",t1.is_alive())
print("Program execution Ended  by :{}".format(threading.current_thread().name))