#Program for Searching  Zero K or One K 
#RegExpr30.py
import re
matdet=re.finditer("K?","KVKKVKKKVKV")
print("-"*50)
for mat in matdet:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(), mat.group()))
print("-"*50)
