#Program for Searching a Word in a given line of Text and find Its First Ocurrence  Stating Index and Ending Index
#RegExpr2.py
import re
line="python is an oop lang.Python is also fun prog lang"
sp="Python"
obj=re.search(sp,line) # Here obj can be either <re.Match> or NoneType
if(obj!=None):
	print("Search is Sucessful")
	print("Starting Index=",obj.start())
	print("Ending Index=",obj.end())
	print("Matched Values=",obj.group())
else:
	print("Search is UnSucessful")
	print("'{}' does not exist in given data".format(sp))
