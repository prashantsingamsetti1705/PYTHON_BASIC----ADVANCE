#Program for finding Sum of N Natural Numbers and their squares also
#ForLoopEx5.py
n=int(input("Enter How Many Natural Nums Sum U want:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("---------------------------")
    print("By using for loop")
    print("---------------------------")
    print("Nat Num\t\tSquares")
    print("---------------------------")
    s=0 # here s is called Aditive Identity
    ss=0 # here s is called Aditive Identity
    for i in range(1,n+1):
        print("\t{}\t\t{}".format(i,i*i))
        s=s+i
        ss=ss+i*i
    else:
        print("---------------------------")
        print("\t{}\t\t{}".format(s,ss))
        print("---------------------------")
    #--------------------------------------------
    print("By using while loop")
    print("---------------------------")
    print("Nat Nums\t\tSquares")
    print("---------------------------")
    s=0
    ss=0
    i=1
    while(i<=n):
        print("\t{}\t\t\t{}".format(i,i*i))
        s=s+i
        ss=ss+i*i
        i=i+1
    else:
        print("---------------------------")
        print("\t{}\t\t\t{}".format(s,ss))
        print("---------------------------")



