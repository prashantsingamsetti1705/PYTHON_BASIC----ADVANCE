#Program for extracting the Marks from Given Text Data
#MarksExtractEx1.py
import re
gd="Rossum got 88 marks , Gosling got 66 marks , Ritche got 65 marks , Travis got 99 marks and Hinter got 56 marks and Kvr got 11 marks"
sp=r"\d{2}"
markslist=re.findall(sp,gd)
print("-"*50)
print("Marks of students:")
print("-"*50)
for marks in markslist:
	print(marks)
print("-"*50)