#MapEx8.py
import sys
dictemp={}
while(True):
    eno=int(input("Enter Employee Number:"))
    sal=float(input("Enter Employee Salary:"))
    dictemp[eno]=sal # Adding Key,Value to dictobject
    ch=input("\t\tDo u want to Insert another Entry (yes/no):")
    if(ch.lower()=="no"):
        break
    if ch.upper() not in ["YES","NO"]:
        print("Plz Learn Typing")
        sys.exit()
print("*"*50)
print("Empno\t\tEmp Salary")
print("*"*50)
for eno,sal in dictemp.items():
    print("\t{}\t\t{}".format(eno,sal))
print("*"*50)
#Update Salary of every emp of dict by 50%
modsal=list(map(lambda x: x[1]+x[1]*50/100, dictemp.items()))
for k,val in zip(dictemp,modsal):
    dictemp[k]=val
print("*"*50)
print("Empno\t\tNew Emp Salary")
print("*"*50)
for eno,sal in dictemp.items():
    print("\t{}\t\t{}".format(eno,sal))
print("*"*50)