#InnerLoopsEx6.py
n=int(input("Enter How Many Tables to display:"))
if(n<=0):
    print("{} is Invalid input".format(n))
else:
    for num in range(1,n+1): # Outer Loop Supply the Value to Inner
        print("-"*50)
        print("Mul Table for :{}".format(num))
        print("-" * 50)
        for i in range(1,11): # Inner Loop--generates the Table
            print("\t{} x {}={}".format(num,i,num*i))
        else:
            print("-" * 50)
    else:
        print("-" * 50)