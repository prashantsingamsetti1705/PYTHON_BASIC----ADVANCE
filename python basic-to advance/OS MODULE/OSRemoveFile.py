#Program removing File Name
#OSRemoveFile.py
import os
try:
    os.remove("E:\\student.jpg")
    print("File Removed--Verify")
except FileNotFoundError:
    print("File Does not Exist")