#Program for Reading the Data continuously from Key Board and Write It to the File
#DynamicFileWriteEx.py
print("Enter the Data to write to the File (Press @ to Stop):")
with open("sumop.py","a") as fp:
    while(True):
        filedata=input()
        if(filedata!="@"):
            fp.write(filedata+"\n")
        else:
            print("Data Written to the File--Verify")
            break
