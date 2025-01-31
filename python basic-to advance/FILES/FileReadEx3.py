#Program for Reading File Name and Display the conetnt of any File
#FileReadEx3.py
def dispfiledata():
    try:
        filename=input("Enter File Name:")
        with open(filename,"r") as fp:
            filedata=fp.readlines()
            print("-------------------------------------")
            print("\tContent of the File")
            print("-------------------------------------")
            for val in filedata:
                print(val,end="")
            print("-------------------------------------")
    except FileNotFoundError:
        print("File Does Not Exist")
#main program
dispfiledata() # Function call