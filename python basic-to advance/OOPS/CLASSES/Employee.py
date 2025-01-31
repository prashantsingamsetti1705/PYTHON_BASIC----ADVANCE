#Employee.py<----File Name and Moudle name
class Emp:
    def getvals(self, eno, ename, sal):
        self.eno = eno
        self.name = ename
        self.sal = sal

    def dispempvals(self):
        print("\t{}\t{}\t{}".format(self.eno, self.name, self.sal))
