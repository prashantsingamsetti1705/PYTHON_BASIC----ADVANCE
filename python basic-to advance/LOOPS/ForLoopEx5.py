#Program for finding Sum of N Natural Numbers
#ForLoopEx5.py
n=int(input("Enter How Many Natural Nums Sum U want:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("---------------------------")
    print("By using for loop")
    print("---------------------------")
    s=0 # here s is called Aditive Identity
    for i in range(1,n+1):
        print("\t{}".format(i))
        s=s+i
    else:
        print("Sum={}".format(s))
        print("---------------------------")
    #--------------------------------------------
    print("By using while loop")
    print("---------------------------")
    s=0
    i=1
    while(i<=n):
        print("\t{}".format(i))
        s=s+i
        i=i+1
    else:
        print("Sum={}".format(s))
        print("---------------------------")



