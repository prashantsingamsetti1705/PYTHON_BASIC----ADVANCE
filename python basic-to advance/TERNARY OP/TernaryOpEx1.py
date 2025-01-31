#Program for Deciding whether the given value is Palindrome or Nor
#TernaryOpEx1.py
value=input("Enter a Value:")
res ="Palindrome"  if value==value[::-1]  else  "Not Palindrome"
print("{} is {}".format(value,res))