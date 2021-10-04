import Listener.listener as listener
import socket


def ConnectToSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    return s


TCP_IP = '127.0.0.1'
TCP_PORT = 5005

serverSocket = ConnectToSocket()

print(serverSocket)

listener.startListener(serverSocket)




