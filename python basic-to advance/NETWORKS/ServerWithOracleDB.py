#A) Write a Server Side Program, In such a way that It should accept a Employee Number  from Client Side Program and 
#  get other details of employee from Database and give those details to Client Side Program.
#ServerWithOracleDB.py
import socket,oracledb as orc
s=socket.socket()
s.bind(("127.0.0.1",8558))
s.listen(1)
while(True):
	try:
		cs,ca=s.accept()
		cdata=cs.recv(1024).decode()
		print("Employee Number adt server Side:{}".format(cdata))
		empno=int(cdata)
		#Write PDBC Code
		con=orc.connect("system/manager@localhost/orcl")
		cur=con.cursor()
		cur.execute("select * from employee where eno=%d" %empno)
		record=cur.fetchone()
		if(record!=None):
			cs.send(str(record).encode())
		else:
			cs.send(("{} Record Number Does Not Exist".format(empno)).encode())
	except ValueError:
		cs.send("Don't Enter alnums,strs and symbols--try again".encode())
	except orc.DatabaseError as db:
		cs.send(("Problem in Oracle DB:"+db).encode())
