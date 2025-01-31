#Program for Demonstrating the Need of continue statement
#ContinueStmtEx3.py
s="PYTHON"
print("By using while Loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("I am from else Part")
print("-------------------------------")
#My Req: display: PYHON
print("By using while Loop")
i=0
while(i<len(s)): # s="PYTHON"
   if s[i] in ["T","O"]:
       i = i + 1
       continue
   print("{}".format(s[i]),end="")
   i = i + 1
else:
    print()
    print("I am from else Part")
print("-------------------------------")