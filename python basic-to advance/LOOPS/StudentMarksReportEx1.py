#StudentMarksReportEx1.py
#Validation for Student Number:100 to 200
while(True):
    sno=input("Enter Student Number:")
    if(sno.isdigit()) and (int(sno) in range(100,201)):
        break
    print("\t{} is Invalid Student Number-try again".format(sno))
#Validation of Name:
while(True):
    sname=input("Enter Student Name:")
    words=sname.split() # ["Guido","Van","Rossum"]
    name=True
    for word in words:
         if(not word.isalpha()):
            name=False
            break
    if(name):
        break
    else:
        print("\t{} is Invalid Name--try again".format(sname))
#Validation of C Lang Marks:
while(True):
    cm=int(input("Enter Marks in C:"))
    if cm in range(0,101):
        break
    else:
        print("\t{} is Invalid Marks in C Lang--Try again".format(cm))

#Validation of C++ Lang Marks:
while(True):
    cppm=int(input("Enter Marks in C++:"))
    if cppm in range(0,101):
        break
    else:
        print("\t{} is Invalid Marks in CPP Lang--Try again".format(cppm))
#Validation of PYTHON Lang Marks:
while(True):
    pym=int(input("Enter Marks in PYTHON:"))
    if pym in range(0,101):
        break
    else:
        print("\t{} is Invalid Marks in PYTHON Lang--Try again".format(pym))
#Calculate totmarks and percent
totmarks=(cm+cppm+pym)
percent=(totmarks/300)*100
if(cm<40) or (cppm<40) or  (pym<40):
    grade="FAIL"
else:
    if(totmarks in range(250,301)):
        grade="DISTINCTION"
    elif(totmarks in range(200,250)):
        grade="FIRST"
    elif(totmarks in range(150,200)):
        grade="SECOND"
    elif(totmarks in range(120,150)):
        grade="THIRD"
#Dipplay the Student Marks report
print("*"*50)
print("\t\tSTUDENT MARKS REPORT")
print("*"*50)
print("\tStudent Number:{}".format(sno))
print("\tStudent Name:{}".format(sname))
print("\tStudent Marks in C:{}".format(cm))
print("\tStudent Marks in C++:{}".format(cppm))
print("\tStudent Marks in PYTHON:{}".format(pym))
print("-"*50)
print("\tTOTAL MARKS :{}".format(totmarks))
print("\tPERCENT OF MARKS:{}".format(percent))
print("\tGRADE={}".format(grade))
print("*"*50)
