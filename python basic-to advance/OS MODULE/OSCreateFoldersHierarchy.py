#Creating Folders Hierarchy
#OSCreateFoldersHierarchy.py
import os
try:
    os.makedirs("C:\\Apple\\Mango\\Kiwi")
    print("Folders Hierarchy Created--verify")
except FileExistsError:
    print("Folders Hierarchy Alerady Exist")