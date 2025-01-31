#Program Listing the Files in Folder
#ListFilesEx3.py
import os
FilesList=os.listdir(".")
print("Total  Number of Files=",len(FilesList))
print("-----------------------------------")
nopf=0
for filename in FilesList:
    if(filename.endswith(".py")):
        print("\t{}".format(filename))
        nopf=nopf+1
print("-----------------------------------")
print("Number of Python Files=",nopf)
print("-----------------------------------")
