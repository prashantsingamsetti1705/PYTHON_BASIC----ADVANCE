#Program for Deciding whether the given number is Prime or Nor from List of Numbers
#ListComprehensionEx4.py
def decideprime(val):
    res=1
    for i in range(2,val):
        if(val%i==0):
            res=0
            break
    return res

#Main Program
print("Enter List of Values Seeperated by space:")
vals=[int(val) for val in input().split() if int(val)>1]
primes=[ val   for val in vals  if decideprime(val) ]
print("List of Given Values:{}".format(vals))
print("List of Primes:{}".format(primes))