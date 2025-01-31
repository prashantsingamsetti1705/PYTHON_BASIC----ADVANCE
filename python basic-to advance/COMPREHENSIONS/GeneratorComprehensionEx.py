#Program Obtaining List of +Ve Values from List of Numerical Values
#GeneratorComprehensionEx.py

lst=[10,-20,30,-40,67,-12,-45,0,56,-45,2,-5,-5]
ps=(val  for val in lst   if val>0 ) # here ps is an object of <class,'generator'>
#Convert generator object into tuple
pse=tuple(ps)
print(pse,type(pse))
