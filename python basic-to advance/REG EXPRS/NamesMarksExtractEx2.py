#Program for extracting the Names and marks from Given Text Data which is Present in File
#NamesMarksExtractEx2.py
import re
try:
	with open("E:\\KVR-PYTHON-9AM\\REG EXPRS\\NOTES\\StudentsMarks.data","r") as fp:
		filedata=fp.read()
		#Apply the Regular Expression
		nameslist=re.findall("[A-Z][a-z]+",filedata)
		markslist=re.findall(r"\d{2}",filedata)
		print("-"*50)
		print("Names of Students\tMarks of students")
		print("-"*50)
		for names,marks in zip(nameslist,markslist):
			print("\t{}\t\t\t{}".format(names,marks))
		print("-"*50)
except FileNotFoundError:
	print("File Does not Exist")

