#Program for Reading List of Values from KBD and Get Only +Ve Values by using filter()
#FilterEx3.py

pos=lambda val:val>0 # Anonymous Functions

#Main Program
print("Enter List of Values Separated BY space:")
lst=[float(val) for val in input().split()] # lst=[10,-20,-34,56,78,0]
pslist=list(filter(pos,lst))
print("Given Elements=",lst)
print("Positive Elements=",pslist)
