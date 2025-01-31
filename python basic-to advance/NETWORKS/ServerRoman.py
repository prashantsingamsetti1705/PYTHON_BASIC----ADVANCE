#ServerRoman.py
import socket
s=socket.socket()
s.bind(("localhost",3333))
s.listen(2)
print("SSP is Ready to Accept any CSP Request:")
while(True):
	try:
		cs,ca=s.accept()
		cdata=cs.recv(1024).decode()
		print("Client Data at Server=",cdata)
		n=int(cdata)
		if(n<=0):
			cs.send( ("{} does not contain Roman Number".format(n)).encode())
		else:
			rn=""
			while(n>=1000):
				rn=rn+"M"
				n=n-1000
			if(n>=900):
				rn=rn+"CM"
				n=n-900
			if(n>=500):
				rn=rn+"D"
				n=n-500
			if(n>=400):
				rn=rn+"CD"
				n=n-400
			while(n>=100):
				rn=rn+"C"
				n=n-100
			if(n>=90):
				rn=rn+"XC"
				n=n-90
			if(n>=50):
				rn=rn+"L"
				n=n-50
			if(n>=40):
				rn=rn+"XL"
				n=n-40
			while(n>=10):
				rn=rn+"X"
				n=n-10
			if(n>=9):
				rn=rn+"IX"
				n=n-9
			if(n>=5):
				rn=rn+"V"
				n=n-5
			if(n>=4):
				rn=rn+"IV"
				n=n-4
			while(n>=1):
				rn=rn+"I"
				n=n-1
			cs.send(rn.encode())
	except ValueError:
		cs.send("Don't Enter alnums,strs and symbols--try again".encode())
	



