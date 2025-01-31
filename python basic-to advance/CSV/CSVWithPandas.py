import pandas as pd
df=pd.read_csv("E:\\KVR-PYTHON-9AM\\CSV\\NOTES\\student.csv")
print(df[df["MARKS"]>3][["NAME","MARKS"]])
print("---------------------------------------")
print(df[df["MARKS"]<3][["NAME","MARKS"]])

