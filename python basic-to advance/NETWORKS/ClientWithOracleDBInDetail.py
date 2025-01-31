#B) Write a Client Side Program in such a way that It should accept employee number from KBD , and get Other details 
  #  from Server Side Program
#ClientWithOracleDBInDetail.py
import socket 
s=socket.socket()
s.connect(("127.0.0.1",8558))
empno=input("Enter Employee Number to view Other Deatils:")
s.send(empno.encode())
empdet=s.recv(1024).decode()
print("-------------------------------------------")
print("Employee Details")
print("-------------------------------------------")
print(empdet)
print("-------------------------------------------")
