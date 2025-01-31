#ClientRoman.py
import socket
s=socket.socket()
s.connect(("localhost",3333))
print("CSP Got Connection from SSP")
n=input("Enter a Number for getting Its Eqv Roman:")
s.send(n.encode())
sdata=s.recv(1024).decode()
print("Roman({})={}".format(n,sdata))
