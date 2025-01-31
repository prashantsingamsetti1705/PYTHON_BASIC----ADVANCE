#Program for Searching A or B or C only
#RegExpr4.py
import re
gd="Ak5#GnRp@7W&BYPQs6!CMx"
sp="[ABC]"
matdet=re.finditer(sp,gd)
print("-"*50)
for mat in matdet:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(), mat.group()))
print("-"*50)