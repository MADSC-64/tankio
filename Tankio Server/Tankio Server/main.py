import Listener.listener as listener
import socket


TCP_PORT = 5005
UDP_PORT = 5000

def connect_to_socket_TCP():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", TCP_PORT))
    s.listen(25)

    return s

def connect_to_socket_UDP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    s.bind(("" ,UDP_PORT))
    return s

serverSocket = connect_to_socket_TCP()

udpSocket = connect_to_socket_UDP()

listener.start_listener_TCP(serverSocket)

listener.start_listener_UDP(udpSocket)





