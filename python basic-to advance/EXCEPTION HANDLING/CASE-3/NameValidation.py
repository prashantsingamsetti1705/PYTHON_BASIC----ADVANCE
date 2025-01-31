#NameValidation.py
from NameExcept import InvalidNameError, ZeroLengthError, SpaceNameError
def validation(name): # name=Guido Va2n Rossum
    if(len(name)==0):
        raise ZeroLengthError
    elif(name.isspace()):
        raise SpaceNameError
    else:
            words = name.split()  # words=["Guido","Van","Rossum"]
            res = True
            for word in words:
                if (not word.isalpha()):
                    res = False
                    break
            if (res):
               return name
            else:
               raise InvalidNameError



