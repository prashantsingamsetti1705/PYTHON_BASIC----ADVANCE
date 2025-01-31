#Server:	(A). Write a  Server Program in such way that It Should a Numerical Value from Client Side Program, Square It and Send the Result to Client Side Program
#ServerSquare.py
import socket
s=socket.socket()
s.bind(("127.0.0.1",8558))
s.listen(2)
print("SSP is Ready to accept any CSP Request")
while(True):
	try:
		cs,ca=s.accept()
		csd=cs.recv(1024).decode()
		print('Val of Client at Server=',csd)
		cv=float(csd)
		res=cv**2
		cs.send(str(res).encode())
	except ValueError:
		cs.send("Don't enter alnums,strs and symbols".encode())
	

