#Program for Writing the Data to the File----write()
#FileWriteEx1.py
with open("stud4.data","a") as fp:
    fp.write(str(100)+"\t")
    fp.write("Rossum"+"\t")
    fp.write(str(77.34)+"\n")
    print("Data Written to the file--verify")