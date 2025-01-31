#Program for Saving Dict Object Data into the JSON File
#To Save Dict Object Data into JSON File, we use  json.dump(dictobj,FilePointer)
#DictObjectToJsonFile.py
import json
dictobj={"EmpNo":100,"Name":"Travis","Sal":5.6,"Author":"Scientist"}
#Choose the json file and Open it into write mode
with open("E:\\KVR-PYTHON-9AM\\JSON\\NOTES\\emp.json","a") as fp:
	json.dump(dictobj,fp)
	print("Dict Object Data Saved in Json File--Verify")

	