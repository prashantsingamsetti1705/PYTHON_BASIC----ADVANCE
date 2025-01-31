#Program for finding Biggest of Three Nums by using Anonymous Functions
#AnonymousFunEx4.py
findbig=lambda k,v,r:k if v<=k>r else v if k<v>=r else r if k<=r>v else "ALL VALUES ARE EQUAL"

#Main Program
print("Enter Three Numbers:")
a,b,c=float(input()),float(input()),float(input())
res=findbig(a,b,c) # Anonymous Function Call
print("Big({},{},{})={}".format(a,b,c,res))