#BreakStmtEx3.py
s="MISSISSIPPI"
print("By using for Loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("else part of for loop")
print("------------------------------------")
#Today : My Req:  MISS  without Using Slicing and Indexing
cnt=0
for ch in s: # s="MISSISSIPPI"
    if(ch=="I"):
        cnt=cnt+1
    if(cnt==2):
        break
    print("{}".format(ch),end="")
else:
    print("else part of for loop")
print()
print("------------------------------------")