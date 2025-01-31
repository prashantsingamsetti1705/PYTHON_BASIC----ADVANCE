#Program for Demonstrating the Need of  Keyword Variable Length Arguments
#PureKeywordVarLengthArgsEx3.py
def findtotalmarks(sno,sname,cls, city="HYD",**submarks):
	print("*"*50)
	print("\tStudent Number:{}".format(sno))
	print("\tStudent Name:{}".format(sname))
	print("\tStudent Class:{}".format(cls))
	print("\tStudent City:{}".format(city))
	print("-"*40)
	if(len(submarks)==0):pass
	else:		
		print("\tSubjects\tMarks")
		print("-"*40)
		totmarks=0
		for subject,marks in submarks.items():
			print("\t{}\t\t{}".format(subject,marks))
			totmarks=totmarks+marks
		print("-"*40)
		print("\tTOTAL MARKS={}".format(totmarks))
		print("-"*40)

#Main Program
findtotalmarks(10,"RS","X",Telugu=70,Hindi=80,English=85,Maths=99,Science=89,Social=90)
findtotalmarks(20,"TR","XII",Sanskrit=99,English=80,Maths=75,Physics=59,Chemistry=58)
findtotalmarks(30,"SS","B.Tech(CSE)",OS=50,DBMS=60,CGI=45)
findtotalmarks(40,"DR","Research")
findtotalmarks(50,"SD","BA","AP",History=60,Eco=77,Civics=60,Geo=56)
#findtotalmarks(60,"SR","BA",History=60,Eco=77,Civics=60,Geo=56,"AP")--SyntaxError: positional argument follows keyword argument
findtotalmarks(60,"SR","BA",History=60,Eco=77,Civics=60,Geo=56,city="AP")
#findtotalmarks(commerce=50,accounts=45,civics=56,"TAMILNADU",70,"Kaushal","B.Com")--SyntaxError: positional argument follows keyword argument
findtotalmarks(commerce=50,accounts=45,civics=56,city="TAMILNADU",sno=70,sname="Kaushal",cls="B.Com")