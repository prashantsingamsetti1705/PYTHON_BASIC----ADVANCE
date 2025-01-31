#Client :    (B) :Write a  Client Program in such way that It Should accept a Message from Key Board, send to Server 
  #                    Side Program and Get Reply  from Server Side Program.
#ClientChat.py
import socket
while(True):
	s=socket.socket()
	s.connect(("127.0.0.1",9999))
	cspmsg=input("Student-->")
	if(cspmsg.lower()=="bye"):
		s.send(cspmsg.encode())
		break
	else:
		s.send(cspmsg.encode())
		sspmsg=s.recv(1024).decode()
		print("KVR-->",sspmsg)
