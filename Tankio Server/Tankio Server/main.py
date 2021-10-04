import Listener.listener as listener
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005


def connect_to_socket_TCP():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    return s

serverSocket = connect_to_socket_TCP()

listener.start_listener_TCP(serverSocket)




