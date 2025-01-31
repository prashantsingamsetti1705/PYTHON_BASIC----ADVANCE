#Program for demonstrating the default thread
#CurrentThreadEx.py
import threading
t=threading.current_thread()  # <_MainThread(MainThread, started 22208)>
print(t.name)
print("----------------------OR--------------------------")
print(threading.current_thread().name)
