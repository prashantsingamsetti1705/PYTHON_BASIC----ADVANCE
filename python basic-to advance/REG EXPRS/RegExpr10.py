#Program for Searching for all   except Lower Case Alphabets
#RegExpr10.py
import re
matdet=re.finditer("[^a-z]","Ak5Y#GnRp@7W&bPQs6!CMx")
print("-"*50)
for mat in matdet:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(), mat.group()))
print("-"*50)
