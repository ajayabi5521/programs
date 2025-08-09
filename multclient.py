import socket
s=socket.socket()
s.connect(('192.168.1.26',5098))
while True:
    n=input(" Type here >>>")
    s.sendall(n.encode())
    if n.lower=="exit":
        break
s.close()    
