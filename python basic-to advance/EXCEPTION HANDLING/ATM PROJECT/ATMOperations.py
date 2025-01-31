#ATMOperations.py
from ATMExcept import DepositError,WithdrawError,InSuffFundError
bal=500.0 # Here bal is called Global Variable
def  deposit():
    damt=float(input("Enter Ur Deposit Amount:"))#----ValueError--alnums/strs/ symbols
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("Ur Account xxxxxx123 Deposited with INR:{}".format(damt))
        print("Now Ur Account xxxxxx123 Balance INR:{}".format(bal))
def withdraw():
    global bal
    wamt = float(input("Enter Ur Withdraw Amount:"))  # ----ValueError--alnums/strs/ symbols
    if(wamt<=0):
        raise WithdrawError
    elif((wamt+500)>bal):
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("Ur Account xxxxxx123 Debited with INR:{}".format(wamt))
        print("Now Ur Account xxxxxx123 Balance INR:{}".format(bal))
def balenq():
    print("Ur Account xxxxxx123 Balance INR:{}".format(bal))
