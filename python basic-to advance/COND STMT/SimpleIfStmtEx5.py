#Program for accepting any digit and display Its Name
#SimpleInfStmtEx4.py--by using simple if statement
d=int(input("Enter Any digit:")) # 0 1 2 3 4 5 6 7 8 9
if(d==0):
    print("{} is ZERO".format(d))
if(d==1):
    print("{} is ONE".format(d))
if(d==2):
    print("{} is TW".format(d))
if(d==3):
    print("{} is THREE".format(d))
if(d==4):
    print("{} is FOUR".format(d))
if(d==5):
    print("{} is FIVE".format(d))
if(d==6):
    print("{} is SIX".format(d))
if(d==7):
    print("{} is SEVEN".format(d))
if(d==8):
    print("{} is EIGHT".format(d))
if(d==9):
    print("{} is NINE".format(d))
if(d>9):
    print("{} is +VE NUMBER".format(d))
if d in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("{} is -VE Digit".format(d))
if(d<0) and d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("{} is -VE Number".format(d))
print("Program execution completed")