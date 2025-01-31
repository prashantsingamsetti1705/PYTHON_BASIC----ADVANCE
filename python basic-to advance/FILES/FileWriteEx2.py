#Program for Writing the Data to the File----writelines()
#FileWriteEx2.py
x= {10:"Python",20:"Java",30:"C",40:"DSA"} # Here x is called Iterable Object
with open("stud5.data","a") as fp:
    fp.writelines(str(x)+"\n")
    print("Data Written to the File--verify")
