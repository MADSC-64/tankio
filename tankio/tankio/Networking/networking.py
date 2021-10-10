import Networking.Http.httpDecoder as decoder
import Networking.Http.httpEncoder as encoder

import socket
import json

server_name = "localhost"
server_port_TCP = 5005
server_port_UDP = 5000

BUFFER_SIZE = 2048

socket_TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send_recieve_to_server_UDP(msg):
    try:
        socket_UDP.sendto(bytes(msg,'utf-8'),(server_name,server_port_UDP))
        socket_UDP.settimeout(2)

        data , addr = socket_UDP.recvfrom(1024)
        print("received echo: ", data)
        print("received at: " , addr )

        return data
    except socket.timeout:
        print("timeout")
        return None

def send_to_server_UDP(msg):
    try:
        socket_UDP.sendto(bytes(msg,'utf-8'),(server_name,server_port_UDP))
    except:
        print("error")


def connect_to_server_TCP():
    try:
        socket_TCP.connect((server_name,server_port_TCP))
    except Exception as e:
        print(e)

def send_http_request(method,url,body):
    try:
        connect_to_server_TCP()

        msg = encoder.generate_Http_response(method,url,body)

        socket_TCP.send(bytes(msg,'utf-8'))

        data = socket_TCP.recv(BUFFER_SIZE)

        return bytes.decode(data,'utf-8')
    except Exception as e:
        print("sending exception :"+str(e))

    return None

def init():
    send_http_request("GET","/","")
