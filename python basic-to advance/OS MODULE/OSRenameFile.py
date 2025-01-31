#Program for Renaming a File
#OSRenameFile.py
import os
try:
    os.rename("hyd.info","hyd.info")
    print("File name Renamed--verify")
except FileNotFoundError:
    print("Source File Name does not Exist")