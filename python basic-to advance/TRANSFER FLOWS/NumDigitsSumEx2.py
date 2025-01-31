#Program for adding digits of Given Number
#NumDigitsSumEx2.py
num=int(input("Enter Any Number:"))
if(num<=0):
    print("{} is invalid input".format(num))
else:
    s=0
    for d in str(num):
        s=s+int(d)
    else:
        print("sum of digits({})={}".format(num,s))
