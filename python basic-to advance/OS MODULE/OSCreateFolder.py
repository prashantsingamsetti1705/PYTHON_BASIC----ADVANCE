#Program for Creating a Folder
# To create a Folder, we use   os.mkdir("File Name")
#OSCreateFolder.py
import os
try:
    os.mkdir("MANGO")
    print("FOlder Created--Verify")
except FileExistsError:
    print("Folder already Exist")
except FileNotFoundError:
    print("Root Folder does not Exist ")