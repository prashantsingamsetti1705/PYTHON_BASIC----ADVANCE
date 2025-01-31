#Program for Counting the Lines,Words and Chars from any File
#FileCountInfo.py
def fileinfo():
    try:
        filename=input("Enter File Name for Counting Its Lines, words and Chars:")
        with open(filename,"r") as fp:
            filedata=fp.readlines()
            nl=0
            nw=0
            nc=0
            for line in filedata:
                nl=nl+1
                nw=nw+len(line.split())
                nc=nc+len(line)
                #For Counting Number of Alphabets-use the following Code
                #for ch in line:
                #    if(ch.isalpha()):
                #        nc=nc+1
            else:
                print("-----------------------------")
                print("Number of Lines={}".format(nl))
                print("Number of Words={}".format(nw))
                print("Number of Chars={}".format(nc))
                print("-----------------------------")
    except FileNotFoundError:
        print("File Does Not Exist")
#Main Program
fileinfo() # Function call