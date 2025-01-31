#InnerLoopsEx8.py
n=int(input("Enter the Range in which u want Prime Numbers:"))
if(n<=1):
    print("{} is Invalid Input".format(n))
else:
    print("-------------------------------")
    print("List of Prime Numbers")
    print("-------------------------------")
    nop=0
    for num in range(2,n+1):#Outer Loop Supply the Number to Inner Loop
        res=True
        for i in range(2,num):
            if(num%i==0):
                res=False
                break
        if(res):
            print("\t{}".format(num))
            nop+=1
    else:
        print("-------------------------------")
        print("Number of Primes within {}={}".format(n,nop))
        print("-------------------------------")