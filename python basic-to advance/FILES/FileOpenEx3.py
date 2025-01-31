#Program for Demonstrating How to Open the File
#FileOpenEx3.py
try:
    with open("stud1.data","r") as fp:
         print("---Inside of with open() as Indentation-----")
         print("\tFile Opened in Read Mode Sucessfully:")
         print("\tFile Opening Mode=",fp.name)
         print("\tFile Opening Mode=",fp.mode)
         print("\tCan we Read the Data from File=",fp.readable())
         print("\tcan we write the Data to the file=",fp.writable())
         print("\tIs File Closed=",fp.closed)
         print("------------------------------------")
    print("\nIs File Closed after out-off with open() as Identation=",fp.closed)
except FileNotFoundError:
    print("File Does not Exist")
