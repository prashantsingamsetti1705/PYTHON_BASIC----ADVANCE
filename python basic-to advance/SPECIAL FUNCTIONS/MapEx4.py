#Program for accepting List of for Two List Object and Find Their sum
#MapEx4.py
def listadd(k,v):
    return (k+v)

#Main Program
print("Enter List of Numerical Values for First List")
lst1=[float(val) for val in input().split()]
print("Enter List of Numerical Values for Second List")
lst2=[float(val) for val in input().split()]
lst3=list(map(listadd,lst1,lst2))
print("*"*50)
print("List1\t\tList2\t\tList3")
print("*"*50)
for L1,L2,L3 in zip(lst1,lst2,lst3):
    print("{}\t\t\t{}\t\t\t{}".format(L1,L2,L3))
print("*"*50)
