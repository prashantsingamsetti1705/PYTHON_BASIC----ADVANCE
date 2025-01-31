#Program for Reading the Student Data from KBD and Save them as Record in File
#StudentPickEx1.py
import pickle
def savestuddata():
    with open("stud.pick","ab") as fp:
        #Read the student Data from KBD
        print("----------------------------------")
        sno=int(input("Enter Student Number:"))
        sname=input("Enter Student Name:")
        marks=float(input("Enter Student Marks:"))
        print("----------------------------------")
        #create an empty list for placing student vals
        lst=[]
        lst.append(sno)
        lst.append(sname)
        lst.append(marks)
        #Save lst data to student.pick file
        pickle.dump(lst,fp)
        print("Student Data Saved in a File Sucessfully")
        print("----------------------------------")

#Main Progra
savestuddata()


