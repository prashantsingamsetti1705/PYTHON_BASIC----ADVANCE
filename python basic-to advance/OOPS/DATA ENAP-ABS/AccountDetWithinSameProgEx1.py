#AccountDetWithinSameProgEx1.py
class Account:
    def __init__(self):
        self.__acno=100
        self.cname="Rossum"
        self.__bal=5.5
        self.__pin=1234
        self.bname="SBI"
    def dispaccdet(self):
        print("-----------------------------")
        print("Account Number:",self.__acno)
        print("Account Holder Number:", self.cname)
        print("Account Balance:",self.__bal)
        print("Account Pin:",self.__pin)
        print("Account Branch Name:", ac.bname)
        print("-----------------------------")



#Main Program
ac=Account() # Object Creation
#print("Account Number=",ac.__acno)Not Possible
#It is Nt Possible to access encspsulated
# Data Members of Account class as part of Main Program
ac.dispaccdet()
