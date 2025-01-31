#MapEx7.py
dictemp={10:1500,11:2000,12:3000,13:1800,14:2000}
print("*"*50)
print("Empno\t\tEmp Salary")
print("*"*50)
for eno,sal in dictemp.items():
    print("\t{}\t\t{}".format(eno,sal))
print("*"*50)
#Update Salary of every emp of dict by 50%
modsal=list(map(lambda x: dictemp[x]+dictemp[x]*50/100, dictemp))
for k,val in zip(dictemp,modsal):
    dictemp[k]=val
print("*"*50)
print("Empno\t\tNew Emp Salary")
print("*"*50)
for eno,sal in dictemp.items():
    print("\t{}\t\t{}".format(eno,sal))
print("*"*50)