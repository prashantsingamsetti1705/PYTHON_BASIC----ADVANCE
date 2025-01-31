#Program for finding sum and average of list of values
#SumAvgFunEx1.py
def findsumavg():
    n=int(input("Enter How Many Values u want to Enter:"))
    if(n<=0):
        print("{} is Invalid Input".format(n))
    else:
        lst=[]
        for i in range(1,n+1):
            value=float(input("Enter {} Value:".format(i)))
            lst.append(value)
        else:
            print("-------------------------------")
            print("\nList of Values:")
            print(lst) # [20.0, 10.0, 30.0, 40.0, 50.0]
            s=0
            for val in lst:
                s=s+val
            else:
                print("Sum={}".format(s))
                print("Avg={}".format(s/len(lst)))
                print("-------------------------------")
#Main Program
findsumavg() # Function call