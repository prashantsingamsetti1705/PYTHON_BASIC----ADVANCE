#Program Obtaining List of +Ve Values from List of Numerical Values
#ListComprehensionEx1.py
lst=[10,-20,30,-40,67,-12,-45,0,56,-45,2,-5,-5]

pslist=[ val  for val in lst   if val>0 ]

nglist=[val for val in lst if val<0]
print("List of +Ve Vals=",pslist,type(pslist))
print("List of -Ve Vals=",nglist,type(nglist))