#Program for Searching  Space Characetr Only
#RegExpr25.py
import re
matdet=re.finditer(r"\s","A k5Y#GnRp @7W&bP)s6!CMx")
print("-"*50)
for mat in matdet:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(), mat.group()))
print("-"*50)
print("Number of Space Characetrs=", len(re.findall(r"\s","A k5Y#GnRp @7W&bP)s6!CMx")))