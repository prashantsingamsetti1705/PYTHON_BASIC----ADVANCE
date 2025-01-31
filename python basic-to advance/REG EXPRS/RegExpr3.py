#Program for Searching a Word in a given line of Text and find Its ALL Ocurrences and get  Stating Index and Ending Index
#RegExpr3.py
import re
line="Python is an oop lang.Python is also fun prog lang"
sp="Python"
matdet=re.finditer(sp,line) # Here matdet is an object of <class 'callable_iterator'>
print("-----------------------------------------------------------------------------")
for mat in matdet: # Here mat is an object of <class, re.match>
	print("Starting Index:{}  End Index:{}   Value:{}".format(mat.start(),mat.end(),mat.group()))
print("-----------------------------------------------------------------------------")