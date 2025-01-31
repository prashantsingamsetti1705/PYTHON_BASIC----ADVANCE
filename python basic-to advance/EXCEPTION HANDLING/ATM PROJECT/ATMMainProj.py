#ATMMainProj.py
from ATMExcept import DepositError, WithdrawError, InSuffFundError
from ATMMenu import menu
from ATMOperations import deposit,withdraw,balenq
while(True):
    menu()
    try:
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except ValueError:
                    print("Don't try to Deposit alnums,strs and symbols")
                except DepositError:
                    print("Don't Enter -Ve and Zero as Deposit Amount")
            case 2:
                try:
                    withdraw()
                except ValueError:
                    print("Don't try to Withdraw alnums,strs and symbols")
                except WithdrawError:
                    print("Don't Enter -Ve and Zero as Withdraw Amount")
                except InSuffFundError:
                    print("Ur Account xxxxxx123 does not have Suff Funds--Read Python Notes")
            case 3:
                balenq()
            case 4:
                print("Thx for this application")
                break
            case _:
                print("Ur Selection of Operation is wrong--try again")
    except ValueError:
        print("Don't enter alnums,strs and symbols for Choice-try again")
