#Program for Searching for all Alpha-numerics only
#RegExpr15.py
import re
matdet=re.finditer("[A-Za-z0-9]","Ak5Y#GnRp@7W&bP)s6!CMx")
print("-"*50)
for mat in matdet:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(), mat.group()))
print("-"*50)
