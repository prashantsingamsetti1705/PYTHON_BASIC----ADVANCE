#ArithmeticCalOops.py
class Arithmetic:
    def getvals(self):
        self.a=float(input("Enter First Value:"))
        self.b = float(input("Enter Second Value:"))
        self.op=input("Enter Any Arithmetic Operator:")
class Calculator:
    @staticmethod
    def cal(ao):  # ao={'a': 10.0, 'b': 2.0, 'op': '**'}
        match(ao.op):
            case "+":
                print("sum({},{})={}".format(ao.a,ao.b,ao.a+ao.b))
            case "-":
                print("sub({},{})={}".format(ao.a, ao.b, ao.a - ao.b))
            case "*":
                print("mul({},{})={}".format(ao.a, ao.b, ao.a * ao.b))
            case "/":
                print("div({},{})={}".format(ao.a, ao.b, ao.a / ao.b))
            case "//":
                print("div({},{})={}".format(ao.a, ao.b, ao.a // ao.b))
            case "%":
                print("mod({},{})={}".format(ao.a, ao.b, ao.a % ao.b))
            case "**":
                print("pow({},{})={}".format(ao.a, ao.b, ao.a ** ao.b))
            case _:
                print("{} is not Arithmetic Operator-try again".format(ao.op))

#Main Program
ao=Arithmetic()
while(True):
    try:
        ao.getvals()
        Calculator.cal(ao) # Calling Static Method w.r.t Class Name
    except ValueError:
        print("Don't enter alnums,strs and symbols--try again")
    else:
        break