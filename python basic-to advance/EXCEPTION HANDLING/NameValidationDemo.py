#NameValidationDemo.py<----Main Program
from NameExcept import InvalidNameError, ZeroLengthError, SpaceNameError
from NameValidation import validation
try:
    name=input("Enter Ur Name:")
    res=validation(name) # Fucntion call give either Result or Exception
except InvalidNameError:

    print("Invalid Name--Try Again")
except ZeroLengthError:
    print("Try to enter Ur Name")
except SpaceNameError:
    print("Don't enter Space for Ur Name--try again:")
else:
    print("{} is Valid Name".format(res))
