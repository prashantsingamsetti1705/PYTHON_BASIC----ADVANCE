#Program for Reading JSON File Data into Dict Object 
#To Read JSON File Data into Dict Object , we use  dictobject=json.load(FilePointer)
#JsonFileToDictObj1.py
import json
try:
	with open("E:\\KVR-PYTHON FOR DSC\\KVR-PANDAS-EXCLUSIVE\\DATAFRAME\\DATA SETS\\data.json","r") as fp:
			dictobj=json.load(fp)
			print("Dict Object Data={}".format(dictobj))
			print("--------------------------------------------------------------------")
			for k ,v in dictobj.items():
				print("{}".format(k))
				for key,val in v.items():
					print("\t{}---->{}".format(key,val))
			print("--------------------------------------------------------------------")
except FileNotFoundError:
	print("File does not Exist")