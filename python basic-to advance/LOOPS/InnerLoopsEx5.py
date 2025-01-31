#InnerLoopsEx5.py
for i in range(1,3): # Outer Loop
    print("=======================================")
    for j in range(1, 4):  # Inner Loop
        print("\tI\tJ\tK")
        for k in range(1, 4):  # Inner-Inner Loop
            print("\t{}\t{}\t{}".format(i,j,k))
        else:
            print("----------------------------------")
    else:
        print("=======================================")