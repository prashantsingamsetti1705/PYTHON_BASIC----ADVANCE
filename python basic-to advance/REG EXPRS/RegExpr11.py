#Program for Searching for Upper  and Lower Case Alphabets only
#RegExpr11.py
import re
matdet=re.finditer("[A-Za-z]","Ak5Y#GnRp@7W&bPQs6!CMx")
print("-"*50)
for mat in matdet:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(), mat.group()))
print("-"*50)
