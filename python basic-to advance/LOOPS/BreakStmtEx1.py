#BreakStmtEx1.py
s="PYTHON"
print("By using for Loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("else part of for loop")
print("------------------------------------")
#Today : My Req:  PYTH  without Using Slicing and Indexing
for ch in s: # s=PYTHON
    if(ch=="O"):
        break
    print("{}".format(ch),end="")
else:
    print("else part of for loop")
print()
print("-------------------------------------------")
