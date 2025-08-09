'''import socket
import threading
s=socket.socket()
s.bind(('192.168.1.26',1298))
s.listen()
def server(conn):
    while True:
            
            data=conn.recv(1024)
        
            print(data.decode())
            conn.close()
        
while True:


    conn, addr=s.accept()
        
    thread=threading.Thread(target=server,args=(conn,)).start()
s.close()'''

import socket
import threading

s = socket.socket()
s.bind(('192.168.1.26', 5098))
s.listen()

def server(conn):
    while True:
        try:
            data = conn.recv(1024)
            print(data.decode())
        except:
            conn.close()
      
while True:
    conn, addr = s.accept()
    threading.Thread(target=server, args=(conn,)).start()

s.close()
