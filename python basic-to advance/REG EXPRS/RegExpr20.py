#Program for Searching for all  except Lower case Alphabets and Digits 
#RegExpr20.py
import re
matdet=re.finditer("[^a-z0-9]","Ak5Y#GnRp@7W&bP)s6!CMx")
print("-"*50)
for mat in matdet:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(), mat.group()))
print("-"*50)

print("Number of Upper case Alphabets and Special symbols =",len(re.findall("[^a-z0-9]","Ak5Y#GnRp@7W&bP)s6!CMx")))