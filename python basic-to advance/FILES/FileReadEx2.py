#Program for Reading File Name and Display the conetnt of any File
#FileReadEx2.py
def dispfiledata():
    try:
        filename=input("Enter File Name to display Its content:")
        with open(filename,"r") as fp:
            filedata=fp.read()
            print("------------------------------")
            print("Content of File")
            print("------------------------------")
            print("{}".format(filedata))
            print("------------------------------")
    except FileNotFoundError:
        print("File Does Not Exist")
#main program
dispfiledata() # Function call