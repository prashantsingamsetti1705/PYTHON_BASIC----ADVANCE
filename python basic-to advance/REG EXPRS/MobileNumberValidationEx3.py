#Program for validating Mobile Number Validation with country code
#MobileNumberValidationEx3.py
import re
while(True):
	mno=input("Enter Ur Mobile Number with country code:")
	if(len(mno)==13):
		res=re.search("\\+9198\\d{8}",mno)
		if(res!=None):
			print("\t{} is Valid Mobile Number".format(mno))
			break
		else:
			print("\t{} is not a Mobile Number----try again".format(mno))
	else:
		print("\t{} is Invalid Mobile Number Length--try again".format(mno))