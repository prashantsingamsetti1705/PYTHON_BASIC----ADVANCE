#Program for Searching only Digits
#RegExpr13.py
import re
matdet=re.finditer("[0-9]","Ak5Y#GnRp@7W&bPQs6!CMx")
print("-"*50)
for mat in matdet:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(), mat.group()))
print("-"*50)
