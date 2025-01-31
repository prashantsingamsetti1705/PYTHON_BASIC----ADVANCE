#Program for Demonstrating the Need of  Keyword Variable Length Arguments
#This Program will  Execute 
#KeywordVarLengthArgsEx2.py
def dispvalues(sno,sname,marks): # Function Def-1 
	print(sno,sname,marks)

dispvalues(sno=100,sname="RS",marks=45.67) # Function Call-1 with 3 Key Word Arguments
#------------------------------------------------------------------------------------------------------------------------------
def dispvalues(eno,ename,job,sal) : # Function Def-2
	print(eno,ename,job,sal)

dispvalues(eno=200,ename="TR",job="SE",sal=8.0) # Function Call-2 with 4 Key Word Arguments
#------------------------------------------------------------------------------------------------------------------------------
def dispvalues(tno,tname,sub1,sub2,sub3):# Function Def-3
	print(tno,tname,sub1,sub2,sub3)

dispvalues(tno=300,tname="JH",sub1="Python",sub2="Java",sub3="DSA") # Function Call-3 with 5 Key Word Arguments
#------------------------------------------------------------------------------------------------------------------------------
def dispvalues(cid,cname):
	print(cid,cname)

dispvalues(cid=400,cname="DR")# Function Call-4 with 2 Key Word Arguments
#------------------------------------------------------------------------------------------------------------------------------



