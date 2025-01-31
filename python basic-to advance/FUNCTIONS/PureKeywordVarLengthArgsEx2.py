#Program for Demonstrating the Need of  Keyword Variable Length Arguments
#PureKeywordVarLengthArgsEx2.py
def dispvalues(**kvr): # Here **kvr is called Var-Length Keyword arg and whose type <class,dict>
	print("-----------------------------------------------")
	print("Number of Values=",len(kvr))
	if(len(kvr)!=0):
		for key,val in kvr.items():
			print("\t{}--->{}".format(key,val))
	else:
		print("Empty Function Call without any Keyword Var length Params")
	print("-----------------------------------------------")



#Main Program
dispvalues(sno=100,sname="RS",marks=45.67) # Function Call-1 with 3 Key Word Arguments
dispvalues(eno=200,ename="TR",job="SE",sal=8.0) # Function Call-2 with 4 Key Word Arguments
dispvalues(tno=300,tname="JH",sub1="Python",sub2="Java",sub3="DSA") # Function Call-3 with 5 Key Word Arguments
dispvalues(cid=400,cname="DR")# Function Call-4 with 2 Key Word Arguments
dispvalues(stno=1000,sname="SS",hb1="Eating",hb2="Sleeping",hb3="Chatting",hb4="Roaming") # # Function Call-5 with 6 Key Word Arguments
dispvalues()