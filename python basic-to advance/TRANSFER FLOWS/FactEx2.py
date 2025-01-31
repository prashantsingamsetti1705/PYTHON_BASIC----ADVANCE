#Program for Cal Factorial of a Given Number
#Case-1:  if n is +Ve----- Fact Cal =  n x n-1 x n-2......0!
#Case-2:  if n is 0 ------- Fact=1
#Case-3:  if n is -ve------Invalid Input
#FactEx2.py
n=int(input("Enter Any Number for Cal Factorial:"))
if(n<0):
    print("{} is Invalid Input".format(n))
else:
    fact=1
    for i in range(n,0,-1):
        fact *=i
    else:
        print("{}!={}".format(n,fact))


