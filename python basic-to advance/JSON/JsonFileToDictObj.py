#Program for Reading JSON File Data into Dict Object 
#To Read JSON File Data into Dict Object , we use  dictobject=json.load(FilePointer)
#JsonFileToDictObj.py
import json
try:
	with open("E:\\KVR-PYTHON-9AM\\JSON\\NOTES\\emp.json","r") as fp:
			dictobj=json.load(fp)
			print("Dict Object Data={}".format(dictobj))
			print("--------------------------------------------------------------------")
			for k in dictobj:
				print("{}--->{}".format(k ,dictobj[k]))
			print("--------------------------------------------------------------------")
except FileNotFoundError:
	print("File does not Exist")

