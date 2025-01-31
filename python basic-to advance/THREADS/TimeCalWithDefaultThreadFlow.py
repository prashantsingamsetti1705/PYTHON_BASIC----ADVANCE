#Program for Demonstrating the Sequential Execution only with Deafult Thread--MainThread
#TimeCalWithDefaultThreadFlow.py
import threading,time
def   square(lst):
	for val in lst:
		print("{}---->square({})={}".format(threading.current_thread().name,val,val**2))
		time.sleep(1)

def   cube(lst):
	for val in lst:
		print("{}---->cube({})={}".format(threading.current_thread().name,val,val**3))
		time.sleep(1)

#Main Program
bt=time.time()
print("Program execution  started by:{}".format(threading.current_thread().name))
print("-"*50)
lst=[2,5,16,17,-19,23,3,14,8]
square(lst)
print("-"*50)
cube(lst)
print("-"*50)
print("Program execution  Ended by:{}".format(threading.current_thread().name))
et=time.time()
print("total execution of time with default thread={}".format(et-bt))