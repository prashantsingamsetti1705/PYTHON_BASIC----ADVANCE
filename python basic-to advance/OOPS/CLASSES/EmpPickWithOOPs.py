#EmpPickWithOOPs.py<---File Name and Acts as Module Name
from Employee import Emp
import pickle
class EmpPick:
    def saveempdata(self):
        with open("oopsemp.pick","ab") as fp:
            while(True):
                try:
                    #read emp values from kbd
                    print("-"*50)
                    eno=int(input("Enter Employee Number:"))
                    ename=input("Enter Employee Name:")
                    empsal=float(input("Enter Employee Salary:"))
                    print("-" * 50)
                    #create an object of Emp of Employee Module
                    eo=Emp()
                    eo.getvals(eno,ename,empsal)
                    #Save eo object data into File by using Pickling
                    pickle.dump(eo,fp)
                    print("Employee Record Saved in File Sucessfully")
                    print("-" * 50)
                    ch=input("Do u want to Insert Another Record(yes/no):")
                    if(ch.lower()=="no"):
                        print("Thx for using this Program")
                        break

                except ValueError:
                    print("\tDon't Enter alnums,strs and symbols for eno and sal-try again")


#Main Program
eo=EmpPick()
eo.saveempdata()



