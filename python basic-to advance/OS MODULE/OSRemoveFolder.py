#Program for Removing a Folder
#OSRemoveFolder.py
import os
try:
    os.rmdir("C:\\KVR")
    print("Folder Removed---verify")
except FileNotFoundError:
    print("Folder Does not Exist")
except OSError:
    print("Ensore Ur Folder Must be Empty")
