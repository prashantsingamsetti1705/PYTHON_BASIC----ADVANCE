#Program for Deciding Whether the Number is Even or Not
#TernaryOpEx2.py
num=int(input("Enter a Number:"))
res = "EVEN" if num%2==0  else  "ODD"
print("{} is {}".format(num,res))