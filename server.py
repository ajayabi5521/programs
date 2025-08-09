import socket
s=socket.socket()
s.bind(('192.168.1.26',12990))
s.listen(1)
conn,_=s.accept()
print(conn.recv(1024).decode())
