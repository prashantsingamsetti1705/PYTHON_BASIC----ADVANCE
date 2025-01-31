#Program for Reading List of Values from KBD and Get Only +Ve Values by using filter()
#FilterEx4.py
print("Enter List of Values Separated BY space:")
lst=[float(val) for val in input().split()] # lst=[10,-20,-34,56,78,0]
pslist=list(filter(lambda val:val>0,lst))
nglist=tuple(filter(lambda x: x<0, lst))
print("Given Elements=",lst)
print("Positive Elements=",pslist)
print("Negative Elements=",nglist)
