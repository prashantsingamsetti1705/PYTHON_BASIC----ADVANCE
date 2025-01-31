#Program for Demonstrating Dict Data to JSON Str Data.
#DictDataToJsonStrData.py
print("-"*70)
d={"EmpNo":100,"Name":"Travis","Sal":5.6,"Author":"Scientist"}
print("Dict Data={}   Type={}".format(d,type(d)))
print("-"*70)
#Covert Dict Object data to JSON Str Data format
jsonstrdata=str(d)
print("Json Str Data={}  Type={}".format(jsonstrdata,type(jsonstrdata)))
print("-"*70)
