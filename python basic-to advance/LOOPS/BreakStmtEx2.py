#BreakStmtEx2.py
s="PYTHON"
print("By using while Loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("else part of  while loop")
print("------------------------------------")
#Today : My Req:  PYTH  without Using Slicing and Indexing
i=0
while(i<len(s)):
    if(s[i]=="O"):
        break
    print("{}".format(s[i]),end="")
    i=i+1
else:
    print("else part of  while loop")
print()
print("------------------------------------")