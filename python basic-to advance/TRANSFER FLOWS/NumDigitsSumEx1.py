#Program for adding digits of Given Number
#NumDigitsSumEx1.py
num=int(input("Enter Any Number:"))
if(num<=0):
    print("{} is invalid input".format(num))
else:
    #num=2389
    s=0
    tn=num # We are pre-serving the Original number in temp Var tn
    while(num>0):
        d=num%10
        s=s+d
        num=num//10
    else:
        print("sum of Digits({})={}".format(tn,s))
