#Program for Searching for all Special Symbols only
#RegExpr16.py
import re
matdet=re.finditer("[^A-Za-z0-9]","Ak5Y#GnRp@7W&bP)s6!CMx")
print("-"*50)
for mat in matdet:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(), mat.group()))
print("-"*50)

print("Number of Special sumbols=",len(re.findall("[^A-Za-z0-9]","Ak5Y#GnRp@7W&bP)s6!CMx")))