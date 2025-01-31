#Program for finding number of threads running in python Program
#ActiveCountEx.py
import threading
print("Active Thread Name=",threading.current_thread().name)
noat=threading.active_count()
print("Number threads which are actively running=",noat)