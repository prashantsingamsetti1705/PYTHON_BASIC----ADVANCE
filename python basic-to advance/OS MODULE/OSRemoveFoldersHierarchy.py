#Program for Removing Folders Hierarchy
#OSRemoveFoldersHierarchy.py
import os
try:
    os.removedirs("C:\\Apple\\Mango\\Kiwi")
    print("FOlders Hierarchy Remove--verify")
except FileNotFoundError:
    print("Folders Hierachy Does not Exist")
except OSError:
    print("Ensore Ur Folder Must be Empty")