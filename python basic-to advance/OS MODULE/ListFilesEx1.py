#Program Listing the Files in Folder
#ListFilesEx1.py
import os
FilesList=os.listdir("C:\\Users\\KVR\\PycharmProjects\\9AMFilesExamples")
print("-----------------------------------")
for filename in FilesList:
    print("\t{}".format(filename))
print("-----------------------------------")
