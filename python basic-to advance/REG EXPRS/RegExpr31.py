#Program for Searching  Each and Every Character
#RegExpr31.py
import re
matdet=re.finditer(".","KVKKVKKKVKV")
print("-"*50)
for mat in matdet:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(), mat.group()))
print("-"*50)
