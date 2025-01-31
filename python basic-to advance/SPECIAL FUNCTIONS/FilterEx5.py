#Program for Accepting List of Values and get Palindrome Words by using filter
#FilterEx5.py
print("Enter List of Values Separated BY space:")
lst=[val for val in input().split()]
plwords=list(filter(lambda val: val==val[::-1], lst))
print("List of Given Values=",lst)
print("List of Palindrome Words=",plwords)