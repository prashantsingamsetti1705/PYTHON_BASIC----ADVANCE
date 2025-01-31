#Program for extracting the Names and marks from Given Text Data
#NamesMarksExtractEx1.py
import re
gd="Rossum got 88 marks , Gosling got 66 marks , Ritche got 65 marks , Travis got 99 marks and Hinter got 56 marks and Kvr got 11 marks"
names=re.findall("[A-Z][a-z]+",gd)
markslist=re.findall(r"\d{2}",gd)
print("-"*50)
print("Names of Students\tMarks of students")
print("-"*50)
for name,marks in zip(names,markslist):
	print("\t{}\t\t\t{}".format(name,marks))
print("-"*50)

