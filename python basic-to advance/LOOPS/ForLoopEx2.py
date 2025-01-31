#Program for Generating N to 1 where N is +VE
#ForLoopEx2.py
n=int(input("Enter How Many Numbers u want to Generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("----------------------------------------")
    print("Numbers from {} to 1".format(n))
    print("----------------------------------------")
    for i in range(n,0,-1):
        print("\t\t{}".format(i))
    else:
        print("----------------------------------------")

