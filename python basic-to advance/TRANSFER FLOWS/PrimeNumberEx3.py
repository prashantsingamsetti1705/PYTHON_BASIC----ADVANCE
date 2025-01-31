#Program for accepting an Integer Value and Decide whether It is Prime or Not
#PrimeNumberEx3.py
n=int(input("Enter a Number:"))
if(n<=1):
    print("{} is Invalid input".format(n))
else:
    res=True
    for i in range(2,(n//2)+1):
        if(n%i==0):
            res=False
            break
    res="Prime" if res else "Not Prime"
    print("{} is {}".format(n,res))