#Program for finding Biggest of Multiple Nums by using Anonymous Functions
#AnonymousFunEx5.py
def kvrmax(lst):
    mv=lst[0]
    for v in lst:
        if(v>mv):
            mv=v
    return mv
def kvrmin(lst):
    minv=lst[0]
    for val in lst:
        if(val<minv):
            minv=val
    return minv

findmax=lambda lst: kvrmax(lst)
findmin=lambda lst: kvrmin(lst)
#Main Program
print("Enter List of Values Separated by Space:")
lst=[float(val) for val in input().split()]
mv=findmax(lst) # Anonymous function call
minv=findmin(lst)
print("max({})={}".format(lst,mv))
print("min({})={}".format(lst,minv))