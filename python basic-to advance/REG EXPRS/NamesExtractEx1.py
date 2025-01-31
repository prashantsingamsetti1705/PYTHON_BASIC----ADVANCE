#Program for extracting the Names from Given Text Data
#NamesExtractEx1.py
import re
gd="Rossum got 88 marks , Gosling got 66 marks , Ritche got 65 marks , Travis got 99 marks and Hinter got 56 marks and Kvr got 11 marks"
sp="[A-Z][a-z]+"
names=re.findall(sp,gd)
print("-"*50)
print("Names of Students:")
print("-"*50)
for name in names:
	print(name)
print("-"*50)