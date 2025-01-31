#Program for Demonstrating the Need of continue statement
#ContinueStmtEx2.py
s="PYTHON"
print("By using For Loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("I am from else Part")
print("-------------------------------")
#My Req: display: PYHN
print("By using For Loop")
for ch in s: # s="PYTHON"
    if(ch=="T") or (ch=="O"):
        continue
    print("{}".format(ch),end='')
else:
    print()
    print("I am from else Part")
print("-------------------------------")