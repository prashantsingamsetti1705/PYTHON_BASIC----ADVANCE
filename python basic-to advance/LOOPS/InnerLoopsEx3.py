#InnerLoopsEx3.py
i=5
while(i>=1): # outer Loop
    print("Outer Loop--Val of i=",i)
    print("-"*50)
    for j in range(3,0,-1): #  Inner Loop
        print("\tInner Loop--Val of j=", j)
    else:
        i=i-1
        print("\tout-off Inner loop")
        print("-" * 50)
else:
    print("\tout-off outer loop")
    print("-" * 50)


