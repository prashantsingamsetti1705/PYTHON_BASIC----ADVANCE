#Program for finding sum and average of list of values
#SumAvgFunEx2.py
def findsumavg():
    n=int(input("Enter How Many Values u want to Enter:"))
    if(n<=0):
        return("{} is Invalid Input".format(n))
    else:
        lst=[]
        for i in range(1,n+1):
            value=float(input("Enter {} Value:".format(i)))
            lst.append(value)
        else:
            s=0
            for val in lst:
                s=s+val
            else:
                return lst,s,s/len(lst)

#Main Program
res=findsumavg() # Function call returns either str type or tuple type
if(type(res)==str):
    print(res)
else:
    print("List of Values:{}".format(res[0]))
    print("Sum={}".format(res[1]))
    print("Avg={}".format(res[2]))
