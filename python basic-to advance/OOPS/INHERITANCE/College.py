#College.py<----File Name and Module Name
from Univ import University
class College(University):
    def getcolldet(self):
        self.cname = input("Enter College Name:")
        self.cloc = input("Enter College Location:")
    def dispcolldet(self):
        print("\t\tCollege Details")
        print("-" * 50)
        print("\t\tCollege Name:{}".format(self.cname))
        print("\t\tCollege Location:{}".format(self.cloc))
        print("-" * 50)
