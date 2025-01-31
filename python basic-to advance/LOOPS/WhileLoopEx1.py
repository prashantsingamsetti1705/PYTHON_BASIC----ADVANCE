#Program for Generating 1 to N Numebrs where N is +VE
#WhileLoopEx1.py
n=int(input("Enter How Many Numbers u want to Generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("--------------------------------")
    print("Numbers within :{}".format(n))
    print("--------------------------------")
    i=1 # InitLization Part
    while(i<=n): # Conditional Part
        print("\t\t{}".format(i))
        i=i+1 # OR i+=1  Updation part
    else:
        print()
        print("--------------------------------")