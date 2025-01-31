#Program for Cal Division of Two Numbers
#Division.py<---File Name and Module Name
from NumberDivisionError import NumberDivisionError
def  divop(a,b):
    if(b==0):
        raise NumberDivisionError # here raise is used for Hitting the exception
    else:
        return (a/b)

#Phase-2: Hitting the exception