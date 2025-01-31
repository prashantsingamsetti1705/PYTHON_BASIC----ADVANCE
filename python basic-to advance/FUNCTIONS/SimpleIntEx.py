#SimpleIntEx.py
#INPUT     : Taking from Function Call
#PROCESS   : Done inside of Function Body
#RESULT    : Inside the Function Body
def simpleint(p,t,r):
    if(p<0) or (t<0) or (r<0):
        print("Invalid Input(s)--Try again")
    else:
        si=(p*t*r)/100
        totamt=p+si
        print("="*50)
        print("Simple Interest={}".format(si))
        print("Total Amount to Pay={}".format(totamt))
        print("=" * 50)
#Main Program
p=float(input("Enter Principle Amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter Rate of Interest:"))
simpleint(p,t,r) # Function Call