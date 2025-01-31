#Program for finding Biggest of Three Nums by using Anonymous Functions
#AnonymousFunEx3.py
findbig=lambda k,v,r:k if k>=v and k>r else v if v>k and v>=r else r if r>=k and r>v else "ALL VALUES ARE EQUAL"

#Main Program
print("Enter Three Numbers:")
a,b,c=float(input()),float(input()),float(input())
res=findbig(a,b,c) # Anonymous Function Call
print("Big({},{},{})={}".format(a,b,c,res))