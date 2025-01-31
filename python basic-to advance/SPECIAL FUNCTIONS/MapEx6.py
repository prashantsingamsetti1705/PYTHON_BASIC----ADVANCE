#Program for accepting List of for Two List Object and Find Their sum
#MapEx6.py
print("Enter List of Numerical Values for First List")
lst1=[float(val) for val in input().split()] # [ 100 200 300 ]
print("Enter List of Numerical Values for Second List")
lst2=[float(val) for val in input().split()] # [100,200,300,400 500 600 700]
if(len(lst1)>len(lst2)):
    for i in range(len(lst1)-len(lst2)):
        lst2.append(0)
elif(len(lst2)>len(lst1)):
    for i in range(len(lst2)-len(lst1)):
        lst1.append(0)
#Code for adding the Elements List1 and List2
lst3=list(map(lambda k,v: k+v,lst1,lst2))
print("*"*50)
print("List1\t\tList2\t\t\tList3")
print("*"*50)
for L1,L2,L3 in zip(lst1,lst2,lst3):
    print("{}\t\t\t{}\t\t\t{}".format(L1,L2,L3))
print("*"*50)

