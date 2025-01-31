#MatchCaseEx3.py
import sys
s="""*********************************************************************
				Temprature Conversion Calculator
*********************************************************************
				1,2. F to C  and  F to K
				3,4  C to F  and  C to K
				5,6 K to F  and K to C
				7. Exit
*********************************************************************"""
print(s)
ch=int(input("Enter Ur Choice:"))
match(ch):
    case 1|2:
        F=float(input("Enter the Temp in terms of F:"))
        C = (F - 32)*(5 / 9)
        K = (F - 32) * (5 / 9) + 273.15
        print("Given Temp in F:{}".format(F))
        print("Eqv Temp in C:{}".format(C))
        print("Eqv Temp in K:{}".format(K))
    case 3|4:
        C = float(input("Enter the Temp in terms of C:"))
        F = C*(9 / 5) + 32
        K = C + 273.15
        print("Given Temp in C:{}".format(C))
        print("Eqv Temp in F:{}".format(F))
        print("Eqv Temp in K:{}".format(K))
    case 5|6:
        K = float(input("Enter the Temp in terms of K:"))
        F = (K-273.15)*(9/5) + 32
        C = K - 273.15
        print("Given Temp in K:{}".format(K))
        print("Eqv Temp in F:{}".format(F))
        print("Eqv Temp in C:{}".format(round(C, 2)))
    case _:
        print("Thx for Using Program")
        sys.exit()
print("Program execution completed")