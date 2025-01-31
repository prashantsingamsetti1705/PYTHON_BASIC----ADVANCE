#Program for Demonstrating the Need of continue statement
#ContinueStmtEx1.py
s="PYTHON"
print("By using For Loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("I am from else Part")
print("-------------------------------")
#My Req: display: PYHON
print("By using For Loop")
for ch in s:
    if(ch=="T"):
        continue
    print("{}".format(ch),end='')
else:
    print()
    print("I am from else Part")
print("-------------------------------")