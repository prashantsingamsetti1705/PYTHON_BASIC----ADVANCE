#ReverseWordsInLine.py
class LineWithWords:
    def __init__(self):
        self.line=input("Enter a line of Text:")
    def reversewords(self):
        words=self.line.split()
        rv=[]
        for word in words:
            rv.append(word[::-1])
        else:
            self.rl=" "
            self.rl=self.rl.join(rv)
#Main Program
lo=LineWithWords()
lo.reversewords()
print("Given Line=",lo.line)
print("Reversed words Line=",lo.rl)