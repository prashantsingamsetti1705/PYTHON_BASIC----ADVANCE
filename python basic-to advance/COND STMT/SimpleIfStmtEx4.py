#Program for Deciding the word whether It is Vowel or not
#SimpleIfStmtEx4.py
word=input("Enter any word:").lower() # apple
if (set(word).isdisjoint(set(list("aeiou")))):
    print("{} is not a Vowel Word".format(word))
if (not set(word).isdisjoint(set(list("aeiou")))):
    print("{} is  a Vowel Word".format(word))