#Program for Demonstrating How to Open the File
#FileOpenEx4.py
with open("stud2.data","a+") as fp:
         print("---Inside of with open() as Indentation-----")
         print("\tFile Opened in Write Mode Sucessfully:")
         print("\tFile Opening Mode=",fp.name)
         print("\tFile Opening Mode=",fp.mode)
         print("\tCan we Read the Data from File=",fp.readable())
         print("\tcan we write the Data to the file=",fp.writable())
         print("\tIs File Closed=",fp.closed)
         print("------------------------------------")
print("\nIs File Closed after out-off with open() as Identation=",fp.closed)
