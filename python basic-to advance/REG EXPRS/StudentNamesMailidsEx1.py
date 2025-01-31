#Program for Extracting Mails from File where File Contains Mail Ids data
#StudentNamesMailidsEx1.py
import re
try:
	with open("E:\\KVR-PYTHON-9AM\\REG EXPRS\\NOTES\\StudentsMails.info","r") as fp:
		mailsdata=fp.read()
		mails=re.findall(r"\S+@\S+",mailsdata)
		nameslist=re.findall("[A-Z][a-z]+",mailsdata)
		print("-"*50)
		print("Names of Students\tMails of students")
		print("-"*50)
		for names,mail in zip(nameslist,mails):
			print("\t{}\t\t{}".format(names,mail))
		print("-"*50)
except FileNotFoundError:
	print("File Does not Exist")