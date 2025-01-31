#Program for Finding Length of each word and also find Highest length word
#WordsLengthFunEx1.py
def readvalues():
    nov=int(input("Enter How Many Words u have:"))
    if(nov<=0):
        return ("{} is invalid input".format(nov))
    else:
        words=[]
        for i in range(1,nov+1):
            word=input("Enter {} Word:".format(i))
            words.append(word)
        else:
            return words

def findlengthwords(words): # words=['Python', 'Java', 'Hyderabad', 'Goa']
    wordlen=dict() # create empty dict for getting word name as key and its length as value
    for word in words:
        wordlen[word]=len(word)
    return wordlen

def highestlengthword(dictobj):
    #the values from dict object by using values()
    vals=dictobj.values()
    mv=max(vals) # here max() is a general pre-defined function
    print("-----------------------------------")
    print("List of Max Length Word(s)")
    print("-----------------------------------")
    for key,value in dictobj.items():
        if(value==mv):
            print("\t{}".format(key))
    else:
        print("-----------------------------------")
#Main Program
res=readvalues()
if (type(res)==str):
    print(res)
else:
    WL=findlengthwords(res) # Function call sending list of words
    highestlengthword(WL) # Function call sending Dict Object


