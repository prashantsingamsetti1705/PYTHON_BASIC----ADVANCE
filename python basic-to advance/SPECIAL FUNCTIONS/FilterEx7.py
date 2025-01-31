#Program  implementaing the Following
#Given Line of Text:      S8tRi4@n%GVa&L2uE
#Expected Output
#----------------------------
#		Obtaing Alphabets: StRinGValuE
#		Obtaing Digits: 842
#		Obtain Special Symbols: @%&
#FilterEx7.py
line=input("Enter Line of Text:")
print("--------------------------------")
print("Given Line=", line)
#Filter alhpas
alphas=list(filter(lambda value:value.isalpha(),line))
#alphas.sort(reverse=True)
print("Alphas={}".format("".join(alphas)))
#Filter Digits
digs=list(filter(lambda value: value.isdigit(),line))
print("Digits={}".format("".join(digs)))
#Filter Special Symbols
spsymbols=list(filter(lambda value:(not value.isalnum()) and (not value.isspace()) , line))
print("Special Symbols={}".format("".join(spsymbols)))
print("--------------------------------")

