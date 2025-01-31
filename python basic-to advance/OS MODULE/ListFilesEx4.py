#Program Listing the Files in Folder
#ListFilesEx3.py
import os
FilesList=os.listdir(".")
print("Total  Number of Files=",len(FilesList))
print("-----------------------------------")
datafiles=list(filter(lambda filename:filename.endswith(".data"), FilesList))
for df in datafiles:
    print("\t{}".format(df))
print("-----------------------------------")
print("Number of Python Files=",len(datafiles))
print("-----------------------------------")
