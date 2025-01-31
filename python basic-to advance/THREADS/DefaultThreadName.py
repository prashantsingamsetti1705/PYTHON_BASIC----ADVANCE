#Program for finding the deafult thread
#DefaultThreadName.py
import threading 
tname=threading.current_thread().name
print("Name of Default Thread=",tname)