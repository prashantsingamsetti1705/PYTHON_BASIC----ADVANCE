#Program for generating Mul table for Number n.
#ForLoopEx3.py
n=int(input("Enter a Number for generating mul table:"))
if(n<=0):
    print("{} is invalid Number".format(n))
else:
    print("="*50)
    print('Mul Table for :{}'.format(n))
    print("=" * 50)
    for i in range(1,11):
        print("\t{} x {}={}".format(n,i,n*i))
    else:
        print("=" * 50)


