#Program for accepting a Line of Text and Extract Only Vowels By using continue stmt
#ContinueStmtEx3.py
line=input("Enter line of Text:")
nov=0
for ch in line:
    if(ch.lower() not in ['a','e','i','o','u'] ):
        continue
    print("{}".format(ch),end='')
    nov=nov+1
print("\nNumber of Vowels=",nov)

