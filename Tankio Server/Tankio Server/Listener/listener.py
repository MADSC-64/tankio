import threading
import time

BUFFER_SIZE = 2048
DEFAULTRESPONSE = "HTTP/1.1 200 OK\nCache-Control: no-cache\nServer: libnhttpd\nConnection: Keep-Alive:"


def listener_thread(server):
    print("Thread: starting")

    while 1:
        conn, addr = server.accept()
        print ('Connection address:', addr)

        data = conn.recv(BUFFER_SIZE)
        print ("received data:", data)
        conn.send(data)  # echo


def startListener(server):
    listener = threading.Thread(target=listener_thread,args=(server,))
    listener.start()