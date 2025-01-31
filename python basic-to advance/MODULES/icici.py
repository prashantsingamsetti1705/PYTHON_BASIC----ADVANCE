#icici.py<----File Name and Module Name
bname="ICICI"
addr="Ampt-HYD" # here bname and addr are called Global Var
def simpleint():
    p = float(input("Enter Principle Amount:"))
    t = float(input("Enter Time:"))
    r = float(input("Enter Rate of Interest:"))
    if(p<0) or (t<0) or (r<0):
        print("Invalid Input(s)--Try again")
    else:
        si=(p*t*r)/100
        totamt=p+si
        print("="*50)
        print("Principle Amount={}".format(p))
        print("Time={}".format(t))
        print("Rate of Interest={}".format(r))
        print("Simple Interest={}".format(si))
        print("Total Amount to Pay={}".format(totamt))
        print("=" * 50)
#Main Program
