#Program for Cal Factorial of a Given Number
#Case-1:  if n is +Ve----- Fact Cal =  1 x 2 x 3 x 4.........x n
#Case-2:  if n is 0 ------- Fact=1
#Case-3:  if n is -ve------Invalid Input
#FactEx1.py
n=int(input("Enter Any Number for Cal Factorial:"))
if(n<0):
    print("{} is Invalid Input".format(n))
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    else:
        print("Factorial({})={}".format(n,fact))

