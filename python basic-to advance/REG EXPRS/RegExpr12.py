#Program for Searching for all except Upper  and Lower Case Alphabets
#RegExpr12.py
import re
matdet=re.finditer("[^A-Za-z]","Ak5Y#GnRp@7W&bPQs6!CMx")
print("-"*50)
for mat in matdet:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(), mat.group()))
print("-"*50)
