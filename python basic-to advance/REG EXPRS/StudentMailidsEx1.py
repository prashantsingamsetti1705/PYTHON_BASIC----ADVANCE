#Program for Extracting Mails from File where File Contains Mail Ids data
#StudentMailidsEx1.py
import re
with open("E:\\KVR-PYTHON-9AM\\REG EXPRS\\NOTES\\StudentsMails.info","r") as fp:
	mailsdata=fp.read()
	mails=re.findall(r"\S+@\S+",mailsdata)
	for mail in mails:
		print(mail)