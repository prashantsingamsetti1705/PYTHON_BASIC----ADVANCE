#MatchCaseEx2.py
s="""*********************************************************************
				Temprature Conversion Calculator
*********************************************************************
				1. F to C
				2. F to K
				3. C to F
				4. C to K
				5. K to F
				6. K to C
				7. Exit
*********************************************************************"""
print(s)
ch=int(input("Enter Ur Choice:"))
match(ch):
    case 1:
        F=float(input("Enter the Temp in terms of F:"))
        C = (F - 32)*(5 / 9)
        print("Given Temp in F:{}".format(F))
        print("Eqv Temp in C:{}".format(C))
    case 2:
        F = float(input("Enter the Temp in terms of F:"))
        K=(F - 32)*(5 / 9) + 273.15
        print("Given Temp in F:{}".format(F))
        print("Eqv Temp in K:{}".format(K))
    case 3:
        C = float(input("Enter the Temp in terms of C:"))
        F = C*(9 / 5) + 32
        print("Given Temp in C:{}".format(C))
        print("Eqv Temp in F:{}".format(F))
    case 4:
        C = float(input("Enter the Temp in terms of C:"))
        K=C + 273.15
        print("Given Temp in C:{}".format(C))
        print("Eqv Temp in K:{}".format(K))
    case 5:
        K = float(input("Enter the Temp in terms of K:"))
        F = (K-273.15)*(9/5) + 32
        print("Given Temp in K:{}".format(K))
        print("Eqv Temp in F:{}".format(F))
    case 6:
        K = float(input("Enter the Temp in terms of K:"))
        C=K - 273.15
        print("Given Temp in K:{}".format(K))
        print("Eqv Temp in C:{}".format(round(C,2)))
    case _:
        print("Thx for Using Program")
