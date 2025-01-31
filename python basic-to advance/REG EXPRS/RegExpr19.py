#Program for Searching for all Lower case Alphabets and Digits only
#RegExpr19.py
import re
matdet=re.finditer("[a-z0-9]","Ak5Y#GnRp@7W&bP)s6!CMx")
print("-"*50)
for mat in matdet:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(), mat.group()))
print("-"*50)

print("Number of lower case Alphabets anddigits =",len(re.findall("[a-z0-9]","Ak5Y#GnRp@7W&bP)s6!CMx")))