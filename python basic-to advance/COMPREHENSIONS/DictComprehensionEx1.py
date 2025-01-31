#Program for Finding Square for Every Value of list of values
#DictComprehensionEx1.py
lst=[3,13,12,9,17,4,3]
d={val:val**2 for val in lst }
print(d,type(d))