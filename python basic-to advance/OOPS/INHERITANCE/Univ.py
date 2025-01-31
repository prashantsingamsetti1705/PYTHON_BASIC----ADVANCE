#Univ.py<---File Name and Module Name
class University:
    def getunivdet(self):
        self.uname=input("Enter University Name:")
        self.uloc=input("Enter University Location:")
    def dispunivdet(self):
        print("-"*50)
        print("\t\tUniversity Details")
        print("-" * 50)
        print("\t\tUniversity Name:{}".format(self.uname))
        print("\t\tUniversity Location:{}".format(self.uloc))
        print("-" * 50)