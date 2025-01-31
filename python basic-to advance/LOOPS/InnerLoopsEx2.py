#InnerLoopsEx2.py
i=1
while(i<=5): # outer Loop
    print("Outer Loop--Val of i=",i)
    print("-"*50)
    j=1
    while(j<=3): #  Inner Loop
        print("\tInner Loop--Val of j=", j)
        j=j+1
    else:
        i=i+1
        print("\tout-off Inner loop")
        print("-" * 50)
else:
    print("\tout-off outer loop")
    print("-" * 50)


