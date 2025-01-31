#Program for Obtaining List of -Ve Values from List of Combination +ve and -ve vals
#ListComprehensionEx2.py
neglst=[ float(val)   for val in input("Enter list of Vals separated by space:").split() if float(val)<0 ]
print("List of -Ve Values")
print(neglst)