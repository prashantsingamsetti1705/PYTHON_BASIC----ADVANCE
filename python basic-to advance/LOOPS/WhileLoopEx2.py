#Program for Generating N to 1 where N is +VE
#WhileLoopEx2.py
n=int(input("Enter How Many Numbers u want to Generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("----------------------------------------")
    print("Numbers from {} to 1".format(n))
    print("----------------------------------------")
    i=n # Initlization Part
    while(i>=1): # Cond Part
        print("\t\t{}".format(i))
        i-=1 # OR i=i-1 Updation Part
    else:
        print("----------------------------------------")

