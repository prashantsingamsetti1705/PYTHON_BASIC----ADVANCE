#Program for Renaming a Folder
#OSRenameFolder.py
import os
try:
    os.rename("C:\\HYD","C:\\KVR")
    print("Folder Renamed--verify")
except FileNotFoundError:
    print("Source Folder Name does not Exist")
except FileExistsError:
    print("Dest Folder alerady exist")