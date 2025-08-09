import socket
s=socket.socket()
s.connect(('192.168.1.26',12990))
s.send(b'Welcome to education 000000000')

