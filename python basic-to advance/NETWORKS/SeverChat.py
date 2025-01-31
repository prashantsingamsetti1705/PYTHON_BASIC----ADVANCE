#Server :   (A) : Write a  Server Program in such way that It Should accept a message from Client Side Program and give 
#                        Reply to the Client Side Program
#SeverChat.py
import socket
s=socket.socket()
s.bind(("127.0.0.1",9999))
s.listen(2)
while(True):
	csock,caddr=s.accept()
	cspmsg=csock.recv(1024).decode()
	print("Student-->:{}".format(cspmsg))
	sspmsg=input("KVR-->")
	csock.send(sspmsg.encode())
	



	
