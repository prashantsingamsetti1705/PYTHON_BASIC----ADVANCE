#Program for Reading List of Values from KBD and Get Only +Ve Values by using filter()
#FilterEx2.py
def pos(val):
    if(val>0):
        return True
    else:
        return False
#Main Program
print("Enter List of Values Separated BY space:")
lst=[float(val) for val in input().split()] # lst=[10,-20,-34,56,78,0]
pslist=list(filter(pos,lst))
print("Given Elements=",lst)
print("Positive Elements=",pslist)
