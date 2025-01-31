#Program for Demonstrating the Need of  Keyword Variable Length Arguments
#PureKeywordVarLengthArgsEx4.py
def findtotalmarks(sno,sname,cls, *vals,city="HYD",**submarks):
	print("@"*40)
	for val in vals:
		print("{}".format(val),end=" ")
	print("\t Number Var Length Values={}".format(len(vals)))
	print()
	print("@"*40)
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
findtotalmarks(10,"RS","X",1,2,3,4,5,Telugu=70,Hindi=80,English=85,Maths=99,Science=89,Social=90)
findtotalmarks(20,"TR","XII",10,20,30,40,Sanskrit=99,English=80,Maths=75,Physics=59,Chemistry=58)
findtotalmarks(30,"SS","B.Tech(CSE)",1.2,2.3,3.4,OS=50,DBMS=60,CGI=45)
findtotalmarks(40,"DR","Research",2,3,4)
findtotalmarks(50,"SD","BA",city="AP",History=60,Eco=77,Civics=60,Geo=56)
#findtotalmarks(60,"SR","BA",History=60,Eco=77,Civics=60,Geo=56,"AP")--SyntaxError: positional argument follows keyword argument
findtotalmarks(60,"SR","BA",0.9,0.8,0.7,0.6,0.5,History=60,Eco=77,Civics=60,Geo=56,city="BANG")
#findtotalmarks(commerce=50,accounts=45,civics=56,"TAMILNADU",70,"Kaushal","B.Com")--SyntaxError: positional argument follows keyword argument

#findtotalmarks("KitKat","CadBurry","KinderJoy",commerce=50,accounts=45,civics=56,city="TAMILNADU",sno=70,sname="Kaushal",cls="B.Com")----SyntaxError
findtotalmarks(70,"Himansu","B,Com","KitKat","CadBurry","KinderJoy",commerce=50,accounts=45,civics=56,city="TAMILNADU")


#NOTE:
#>>> sno,sname,*marks=10,"RS",70,80,90,77
#>>> print(sno)-----------------------10
#>>> print(sname)--------------------RS
#>>> print(marks,type(marks))---------[70, 80, 90, 77] <class 'list'>

#NOTE:
#>>> sno,sname,**submarks=10,"SR",C=30,CPP=40,PY=67-------   sno,sname,**submarks=10,"SR",C=30,CPP=40,PY=67
              
#>>> *marks=10,20,30,40,50--------------------SyntaxError: starred assignment target must be in a list or tuple
#>>> sno,*marks=100,1.3,1.4,3.4
#>>> print(sno,marks)----------------100 [1.3, 1.4, 3.4]
