#Program for Copying the Content of One File into Another File
#E:\KVR-PYTHON-9AM\FILES\NOTES
def filecopy():
    try:
        srcfile=input("Enter Source File Name:")
        with open(srcfile,"r") as rp: # Open the Source File in READ MODE
            dstfile=input("Enter Destination File:")
            with open(dstfile,"a") as wp: # Open the Destination File in WRITE MODE
                srcfiledata=rp.read() # read the Data from SOURCE FILE
                wp.write(srcfiledata) # write the source file data to destination file
                print("SRC File Data Copied into Dest File--verify")
    except FileNotFoundError:
        print("Source File does not Exist")

#Main Program
filecopy()