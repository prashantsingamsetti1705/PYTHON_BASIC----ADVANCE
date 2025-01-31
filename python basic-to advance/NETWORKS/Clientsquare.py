#Client:	(B). Write a  Client Program in such way that It Should accept a Numerical Value from Key Board 
# send to Server Side Program and Get Its Square from Server Side Program.
#Clientsquare.py
import socket
s=socket.socket()
s.connect(("localhost",8558))
print("CSP got Connection SSP")
n=input("Enter a Number for getting its Square:")
s.send(n.encode())
sres=s.recv(1024).decode()
print("square({})={}".format(n,sres))