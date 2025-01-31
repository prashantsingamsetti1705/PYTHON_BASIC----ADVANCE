#BreakStmtEx4.py
s="MISSISSIPPI"
print("By using while Loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("else part of for loop")
print("------------------------------------")
#Today : My Req:  MISSI  without Using Slicing and Indexing
cnt=0
i=0
while(i<len(s)): # s="MISSISSIPPI"
    if(s[i]=="S"):
        cnt=cnt+1
    if(cnt==3):
        break
    print("{}".format(s[i]),end="")
    i=i+1
else:
    print("else part of while loop")
print()
print("------------------------------------")