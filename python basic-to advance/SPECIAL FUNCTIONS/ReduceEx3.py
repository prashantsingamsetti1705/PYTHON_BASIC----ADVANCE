#Program for Finding Max and Min from List of Values by using reduce()
#ReduceEx3.py
import functools
print("Enter List of Values Separated By Space:")
lst=[float(val) for val in input().split()] # lst=[10,20,15,25,18,35,2]

maxv=functools.reduce(lambda k,v : k if k>v else v , lst)
minv=functools.reduce(lambda k,v : k if k<v else v , lst)
print("Max({})={}".format(lst,maxv))
print("Min({})={}".format(lst,minv))


