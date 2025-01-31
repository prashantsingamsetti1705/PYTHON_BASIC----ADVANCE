#Program for generating Mul table for Number n.
#WhileLoopEx3.py
n=int(input("Enter a Number for generating mul table:"))
if(n<=0):
    print("{} is invalid Number".format(n))
else:
    print("="*50)
    print('Mul Table for :{}'.format(n))
    print("=" * 50)
    i=1
    while(i<11):
        print("\t{} x {} = {}".format(n,i,n*i))
        i=i+1
    else:
        print("=" * 50)

