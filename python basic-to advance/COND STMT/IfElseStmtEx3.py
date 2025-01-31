#Program for accepting any digit and display Its Name
#IfElseStmtEx3.py--by using if..else statement
d=int(input("Enter Any digit:")) # 0 1 2 3 4 5 6 7 8 9
if(d==0):
    print("{} is ZERO".format(d))
else:
    if (d == 1):
        print("{} is ONE".format(d))
    else:
        if (d == 2):
            print("{} is TWO".format(d))
        else:
            if (d == 3):
                print("{} is THREE".format(d))
            else:
                if (d == 4):
                    print("{} is FOUR".format(d))
                else:
                    if (d == 5):
                        print("{} is FIVE".format(d))
                    else:
                        if (d == 6):
                            print("{} is SIX".format(d))
                        else:
                            if (d == 7):
                                print("{} is SEVEN".format(d))
                            else:
                                if (d == 8):
                                    print("{} is EIGHT".format(d))
                                else:
                                    if (d == 9):
                                        print("{} is NINE".format(d))
                                    else:
                                        if (d >9):
                                            print("{} is +VE NUMBER".format(d))
                                        else:
                                            if (d < 0) and d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
                                                    print("{} is -VE Number".format(d))
                                            else:
                                                if d  in [-1, -2, -3, -4, -5, -6, -7, -8, -9]:
                                                    print("{} is -VE DIGIT ".format(d))
print("Program Execution Compelted")