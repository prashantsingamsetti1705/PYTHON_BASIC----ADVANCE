#InnerLoopsEx1.py
for i in range(1,6):# Outer Loop
    print("Outer Loop--Val of i=",i)
    print("-"*50)
    for j in range(1,4): # Inner Loop
        print("\tInner Loop--Val of j=", j)
    else:
        print("\tout-off Inner loop")
        print("-" * 50)
else:
    print("\tout-off outer loop")
    print("-" * 50)


