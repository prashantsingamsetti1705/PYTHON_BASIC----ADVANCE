#Program for Demonstrating the JSON String Format
#JsonDataToDictData.py
import json
jsondata='{"STNO":"100","NAME":"ROSSUM","MARKS":"78.99"}'
print("-"*70)
print("Json data={}  Type={}".format(jsondata,type(jsondata)))
print("-"*70)
#Convert JsonData into Dict Type by using    loads()
#Syntax:  DictObject=json.loads(jsonstrdata)
d=json.loads(jsondata)
print("Dict Data={}   Type={}".format(d,type(d)))
print("-"*70)
for k,v in d.items():
	print("\t{}--->{}".format(k,v))
print("-"*70)


