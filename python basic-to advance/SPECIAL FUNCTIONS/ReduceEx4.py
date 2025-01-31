#Program for acceping list of words separated by comma and get single of line of Text
#ReduceEx4.py
import functools
print("Enter List of Words Separated by Comma:")
words=[word for word in input().split(",")] #words=["Python","is","an","oop","lang"]
line=functools.reduce(lambda k,v:k+" "+v,words)
print("Line=",line)
