#Program Listing the Files in Folder
#ListFilesEx2.py
import os
FilesList=os.listdir(".")
print("-----------------------------------")
for filename in FilesList:
    print("\t{}".format(filename))
print("-----------------------------------")
