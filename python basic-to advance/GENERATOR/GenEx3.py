#Program for Demonstrating Geemrators
#GenEx3.py
def kvrrange(start,stop=0,step=1):
	if(start>stop):
		stop=start
		start=0
	while(start<=stop):
		yield start
		start=start+step

#Main Program
r1=kvrrange(10,100,10)  # generator Function call-1
for val in r1:
	print(val,end="  ")
print("\n------------------------------------------------")
r2=kvrrange(1000,1006)  # generator Function call-2
for val in r2:
	print(val,end="  ")
print("\n------------------------------------------------")
r2=kvrrange(5)  # generator Function call-3
for val in r2:
	print(val,end="  ")
print("\n------------------------------------------------")
