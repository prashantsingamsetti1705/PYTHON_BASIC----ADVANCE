#EmpUnPickWithOOPs.py
import pickle
class EmpUnPick:
    def readrecords(self):
        try:
            with open("oopsemp.pick","rb") as fp:
                print("-" * 50)
                while(True):
                    try:
                        record=pickle.load(fp)
                        record.dispempvals()
                    except EOFError:
                        print("-"*50)
                        break

        except FileNotFoundError:
            print("File Does not exist")
#Main Program
e=EmpUnPick()
e.readrecords()