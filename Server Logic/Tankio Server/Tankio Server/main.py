import socket

def ConnectToSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    return s


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048
DEFAULTRESPONSE = "HTTP/1.1 200 OK\nCache-Control: no-cache\nServer: libnhttpd\nConnection: Keep-Alive:"

serverSocket = ConnectToSocket()

conn, addr = serverSocket.accept()
print ('Connection address:', addr)
while 1:
     data = conn.recv(BUFFER_SIZE)
     if not data: break
     print ("received data:", data)
     conn.send(data)  # echo
conn.close()




