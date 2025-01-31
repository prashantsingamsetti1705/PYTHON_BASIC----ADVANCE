#Program for accepting List of Values and find sum by using reduce()
#ReduceEx2.py
import functools
print("Enter List of Values Separated By Space:")
lst=[float(val) for val in input().split()]
res=functools.reduce(lambda k,v: k+v,lst)
print("Sum({})={}".format(lst,res))