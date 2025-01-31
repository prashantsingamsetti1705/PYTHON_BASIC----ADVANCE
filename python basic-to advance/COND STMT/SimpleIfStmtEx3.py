#Program for Deciding the word whether It is Vowel or not
#SimpleIfStmtEx3.py
word=input("Enter any word:").lower() # apple
if ('a'in word) or ('e'in word) or ('i'in word) or ('o'in word) or ('u'in word):
    print("{} is a Vowel Word".format(word))
if ('a' not in word) and ('e'not in word) and ('i' not in word) and ('o' not in word) and ('u' not in word):
    print("{} is not a Vowel Word".format(word))
