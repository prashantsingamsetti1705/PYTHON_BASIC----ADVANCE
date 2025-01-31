#Program which will search String Literal within  a String
#SearchStringLiteral.py
import re
patterns=["fox","dog","horse"]
text="The Quick brown fox  jumps over the lazy dog"
for val in patterns:
	print("Searching for '{}' in '{}' ".format(val,text))
	res=re.search(val,text)
	if(res!=None):
		print("'%s' Matched--search is sucessful" %val)
	else:
		print("'%s' Not Matched--search is un-sucessful" %val)
