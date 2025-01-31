#Program for accepting the Salaries of emp and give 50% Hike to every EMP
#MapEx3.py
print("Enter Emp Salaries separated By Space ")
oldsal=[float(sal) for sal in input().split() if float(sal)>0]
newsal=list(map(lambda sal: sal+sal*50/100, oldsal))
print("*"*50)
print("Old Salary\t\tNew Salary")
print("*"*50)
for osl,nsl in zip(oldsal,newsal):
    print("\t{}\t\t{}".format(osl,nsl))
print("*"*50)