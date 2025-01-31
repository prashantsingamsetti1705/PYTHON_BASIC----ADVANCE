#Program for Demonstrating How to Open the File
#FileOpenEx1.py
try:
    fp=open("stud3.data","r")
except FileNotFoundError:
    print("File Does not Exist")
else:
    print("Type of fp=", type(fp))
    print("File Opened in Read Mode")
    print("Is File Closed=",fp.closed)
    print("-------------------------------")
finally:
    print("i am from finally block")
    try:
        print("Is File Closed in finally block=", fp.closed)
        fp.close() # Manual Closing
        print("Is File Closed in finally block after close()=", fp.closed)
    except NameError:
        print("File unable to open-there is no need to close")

