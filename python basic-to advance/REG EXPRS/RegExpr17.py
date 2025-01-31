#Program for Searching for Upper case Alphabets and Digits only
#RegExpr17.py
import re
matdet=re.finditer("[A-Z0-9]","Ak5Y#GnRp@7W&bP)s6!CMx")
print("-"*50)
for mat in matdet:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(), mat.group()))
print("-"*50)

print("Number of Upper case Alphabets and Digits =",len(re.findall("[A-Z0-9]","Ak5Y#GnRp@7W&bP)s6!CMx")))