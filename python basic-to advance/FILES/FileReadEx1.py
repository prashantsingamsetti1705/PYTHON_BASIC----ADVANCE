#Program for Reading and Display the conetnt of any File
#FileReadEx1.py
try:
    with open("stud5.data","r") as fp:
        filedata=fp.read()
        print(type(filedata))
        print("------------------------------")
        print("Content of File")
        print("------------------------------")
        print("{}".format(filedata))
        print("------------------------------")
except FileNotFoundError:
    print("File Does Not Exist")