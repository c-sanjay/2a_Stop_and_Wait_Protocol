import socket
s=socket.socket()
s.connect(('localhost',8001))
print(s.getsockname())
print(s.recv(1024).decode())
s.send("acknowledgement recived from the server".encode())
