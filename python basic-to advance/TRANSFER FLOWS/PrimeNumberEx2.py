#Program for accepting an Integer Value and Decide whether It is Prime or Not
#PrimeNumberEx2.py
n=int(input("Enter a Number:"))
if(n<=1):
    print("{} is Invalid input".format(n))
else:
    res="PRIME"
    for i in range(2,(n//2)+1):
        if(n%i==0):
            res="NOT PRIME"
            break

    print("{} is {}".format(n,res))