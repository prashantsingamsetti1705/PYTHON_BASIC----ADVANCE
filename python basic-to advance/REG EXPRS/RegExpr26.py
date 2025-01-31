#Program for Searching  Space Characetr Only
#RegExpr26.py
import re
matdet=re.finditer(r"\S","A k5Y#GnRp @7W&bP)s6!CMx")
print("-"*50)
for mat in matdet:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(), mat.group()))
print("-"*50)
print("Number of Space Characetrs=", len(re.findall(r"\S","A k5Y#GnRp @7W&bP)s6!CMx")))