#Program for Demonstrating Sub thread creation and dispatching the sub thread
#SubThreadStartEx.py
import threading
def  greet(val):
	print("{}-->Hi:{} Good Morning".format(threading.current_thread().name,val))


#Main Program
t1=threading.Thread(target=greet,args=("Rossum",) )
print("Number of Threads in Program=",threading.active_count()) # 1 
# Here t1 is object whose default name Thread-1 and It is called Sub Thread
print("Execution Status of Sub thread t1=",t1.is_alive())
#Dispatching the Sub Thread(s)
t1.start()
print("Number of Threads in Program=",threading.active_count()) # 2
