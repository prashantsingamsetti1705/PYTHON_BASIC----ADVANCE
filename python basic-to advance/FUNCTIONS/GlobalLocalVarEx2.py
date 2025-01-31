#Program for Understanding the Need of Global Variables
#GlobalLocalVarEx2.py
lang="PYTHON" # Here lang is calleg Global Var
def learnAI():
	sub1="AI"
	print("To Develop '{}' Based Application, we use '{}' Coding".format(sub1,lang))
	#print(sub2)----Invalid bcoz sub2 is local in learnML()

def learnML():
	sub2="ML"
	print("To Develop '{}' Based Application, we use '{}' Coding".format(sub2,lang))
	#print(sub1)--------Invalid bcoz sub1 is local in learnAI()

#Main Program
learnAI()   # Func Call
learnML() # Func Call



