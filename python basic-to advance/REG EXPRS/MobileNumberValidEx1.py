#Program for Validation of Mobile Number
#MobileNumberValidEx1.py
import re
while(True):
	mno=input("Enter Ur Mobile Number:")
	if(len(mno)==10):
		res=re.search(r"\d{10}",mno)
		if(res!=None):
			print("\t{} is a Valid Mobile Number:".format(mno))
			break
		else:
			print("\t{} is Invalid Mobile Number and It must Contain integer Values-try Again".format(mno))
	else:
		print("\t{} is Invalid Mobile Number Length-try again".format(mno))

