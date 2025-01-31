#Program for Demonstrating Sub thread creation and dispatching the sub thread
#SetGetEx.py
import threading
def  greet(val):
	print("{}-->Hi:{} Good Morning".format(threading.current_thread().name,val))


#Main Program
t1=threading.Thread(target=greet,args=("Rossum",) )
#tname=t1.getName()----This Method deprecated on the name of 'name' attribute
#Here and after instead of using getName(), we must use 'name' attribute
print("Default Sub Thread Name before setting =",t1.name)  # get the thread name
#set programmer-Defined thread name to the sub thread
#t1.setName("Pragnadeep")  This Method deprecated on the name of 'name' attribute
#Here and after instead of using setName(), we must use 'name' attribute
t1.name="Pdeep" # Set the thread name
print("Default Sub Thread Name after setting =",t1.name)
#dispatch the sub thread
t1.start()