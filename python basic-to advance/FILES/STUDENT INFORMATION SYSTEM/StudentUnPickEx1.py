#Program for Reading the Student Records from stud.pick file by using un-Pickling Process
#StudentUnPickEx1.py
import pickle
def getallrecords():
    try:
        with open("NIT.data","rb") as fp:
            print("-"*50)
            print("\tStudent Details")
            print("-" * 50)
            while(True):
                try:
                    record=pickle.load(fp)
                    for val in record:
                        print("\t{}".format(val),end="\t")
                    print()
                except EOFError:
                    print("-" * 50)
                    break
    except FileNotFoundError:
        print("File does not exist")

