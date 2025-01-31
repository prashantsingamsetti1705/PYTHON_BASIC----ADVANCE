#A) Write a Server Side Program, In such a way that It should accept a Employee Number  from Client Side Program and 
#  get other details of employee from Database and give those details to Client Side Program.
#ServerWithOracleDBInDetail.py
import socket,oracledb as orc
s=socket.socket()
s.bind(("127.0.0.1",8558))
s.listen(1)
while(True):
	try:
		cs,ca=s.accept()
		cdata=cs.recv(1024).decode()
		print("Employee Number at server Side:{}".format(cdata))
		empno=int(cdata)
		#Write PDBC Code
		con=orc.connect("system/manager@localhost/orcl")
		cur=con.cursor()
		cur.execute("select * from employee where eno=%d" %empno)
		record=cur.fetchone()
		if(record!=None):
			s0="-------------------------------------------------------"
			s1="Employee Number:{}".format(record[0])
			s2="Employee Name:{}".format(record[1])
			s3="Employee Salary:{}".format(record[2])
			s4="Employee Comp Name:{}".format(record[3])
			s5="-------------------------------------------------------"
			res=s0+"\n"+s1+"\n"+s2+"\n"+s3+"\n"+s4+"\n"+s5
			cs.send(res.encode())
		else:
			cs.send(("{} Record Number Does Not Exist".format(empno)).encode())
	except ValueError:
		cs.send("Don't Enter alnums,strs and symbols--try again".encode())
	except orc.DatabaseError as db:
		cs.send(("Problem in Oracle DB:"+db).encode())
