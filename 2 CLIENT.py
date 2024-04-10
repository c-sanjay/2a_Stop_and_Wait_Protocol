import socket
from datetime import datetime
s=socket.socket()
s.bind(('localhost',8001))
s.listen(5)
c,addr=s.accept()
print("Client Address : ",addr)
now = datetime.now()
c.send(now.strftime("Date: %d/%m/%Y and Time: %H:%M:%S").encode())
ack=c.recv(1024).decode()
if ack:
 print(ack)
c.close()
