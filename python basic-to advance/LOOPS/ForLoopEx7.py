#Program for finding Product of N Natural Numbers
#ForLoopEx7.py
n=int(input("Enter How Many Natural Nums Product U want:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("---------------------------")
    print("By using for loop")
    print("---------------------------")
    s=1 # here s is called Multiplicative Identity
    for i in range(1,n+1):
        print("\t{}".format(i))
        s=s*i
    else:
        print("Product={}".format(s))
        print("---------------------------")
    #--------------------------------------------
    print("By using while loop")
    print("---------------------------")
    s=1
    i=1
    while( i <= n ):
        print("\t{}".format(i))
        s=s*i
        i=i+1
    else:
        print("Product={}".format(s))
        print("---------------------------")
