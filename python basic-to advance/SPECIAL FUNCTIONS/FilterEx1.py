#Program for Reading List of Values from KBD and Get Only +Ve Values by using filter()
#FilterEx1.py
def pos(val):
    if(val>0):
        return True
    else:
        return False

#Main Program
print("Enter List of Values Separated BY space:")
lst=[float(val) for val in input().split()] # lst=[10,-20,-34,56,78,0]
obj1=filter(pos,lst)
print("type of obj1=",type(obj1)) #  <class 'filter'>
print("Content of obj",obj1) # <filter object at 0x00000238798C42B0>
#Convert Filter Object obj1 into any Iterable Object--say list
pslist=list(obj1)
print("Given Elements=",lst)
print("Positive Elements=",pslist)
