#Program for Demonstrating the Need of Random Access Files
#RandomAccessFileEx.py
#Filepoiner.seek(Index)---Used for Making the File Pointer to Point to Perticular Index
#FilePointer.tell()----->Used for Obtaining Index of File Pointer where It is Pointing
with open("Hyd.info","r") as fp:
    print("Initial Position ponited by fp=",fp.tell()) # 0
    filedata=fp.read(3)
    print(filedata)
    print("Now Position ponited by fp=", fp.tell())  # 3
    filedata = fp.read(8)
    print(filedata)
    print("Now Position ponited by fp=", fp.tell())  #
    filedata = fp.read(7)
    print(filedata)
    print("Now Position ponited by fp=", fp.tell())  #
    print("--------------------------------")
    filedata=fp.read()
    print(filedata)
    print("Now Position ponited by fp=", fp.tell())  #
    print("--------------------------------")
    #Re-Set the File Ponter Object to 11th Index
    fp.seek(11)
    filedata = fp.read(7)
    print(filedata)
    print("Now Position ponited by fp=", fp.tell())  #
    print("--------------------------------")
    # Re-Set the File Ponter Object to 0th Index
    fp.seek(0)
    filedata = fp.read(110)
    print(filedata)
    print("Now Position ponited by fp=", fp.tell())  #
    print("--------------------------------")
