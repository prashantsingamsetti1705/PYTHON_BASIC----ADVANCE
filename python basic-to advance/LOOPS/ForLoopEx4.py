#Program for accepting a word and Display their Chars
#ForLoopEx4.py
word=input("Enter any Word:")
#Req1: Ex: Python----> p  y  t  h   o  n Line by line
print("-------------------------------------")
print("with for Loop--word in Firward Direction")
print("-------------------------------------")
print("By using for Loop -Logic-1")
for ch in word:
    print("\t{}".format(ch))
print("-------------------------------------")
print("By using for Loop -Logic-2")
for i in range(len(word)):
    print("\t{}".format(word[i]))
print("-------------------------------------")
print("By using for Loop -Logic-3")
for i in range(-len(word),0):
    print("\t{}".format(word[i]))
print("===========================================")
print("with for Loop--word in backward Direction")
print("-------------------------------------")
print("By using for Loop -Logic-1")
print("-------------------------------------------")
for ch in word[::-1]:
    print("\t{}".format(ch))
print("-------------------------------------------")
print("By using for Loop -Logic-2")
print("-------------------------------------------")
for i in range(len(word)-1,-1,-1):
    print("\t{}".format(word[i]))
print("-------------------------------------------")
print("By using for Loop -Logic-3")
print("-------------------------------------------")
for i in range(-1,-(len(word)+1),-1):
    print("\t{}".format(word[i]))
print("-------------------------------------------")
