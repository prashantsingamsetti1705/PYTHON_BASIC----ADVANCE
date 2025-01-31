#Program for Showing the Internal Flow of Default Thread
#DefaultThreadFlow.py
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
print("Line-14")
welcome()
print("Line-16")
hello()
print("Line-18")
hi()
print("Line-20")
print("-------------------------------------------------------")
print("Program execution Ended by:{}".format(threading.current_thread().name))
print("-------------------------------------------------------")
