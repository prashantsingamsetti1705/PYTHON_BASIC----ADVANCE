#Program for Reading the employee data and Writing the Data to the File
#FileWriteEx3.py
#Read the emp data from File
while(True):
    print("-----------------------------------")
    empno=int(input("Enter Employee Number:"))
    empname=input("Enter Employee Name:")
    empsal=float(input("Enter Employee Salary:"))
    print("-----------------------------------")
    #Choose the File Name and Open it into Write Mode
    with open("D:\\KVR\\emp.data","a") as fp:
        fp.write(str(empno)+"\t")
        fp.write(empname+"\t")
        fp.write(str(empsal)+"\n")
        print("Data Written to the File---Verify")
    print("------------------------------------------")
    ch=input("Do u want to Insert Another Record(yes/no):")
    if(ch.lower()=="no"):
        print("Thx for using this Program")
        break
