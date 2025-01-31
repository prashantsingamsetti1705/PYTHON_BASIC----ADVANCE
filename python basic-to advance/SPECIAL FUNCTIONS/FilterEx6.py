#Program for Accepting List of words and find Vowel Words
#FilterEx6.py
print("Enter List of Values Separated BY space:")
words=[val for val in input().split()]
vwords=list(filter(lambda word:"a" in word.lower() or 'e' in word.lower() or 'i' in word.lower() or 'o'in word.lower() or 'u' in word.lower(), words))
print("Given Words=",words)
print("Vowel Words=",vwords)