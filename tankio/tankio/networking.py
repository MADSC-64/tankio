import requests
import socket
import json

server_name = "http://localhost:5005"
server_host = "localhost"
server_port_TCP = 5005
server_port_UDP = 5000

BUFFER_SIZE = 2048

def send_recieve_to_server_UDP(msg):
    try:
        socket_UDP.sendto(bytes(msg,'utf-8'),(server_host,server_port_UDP))
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



def send_http_request(method,target_url,body):
    try:
        request = None

        if method == "POST":
            request = requests.post(server_name+target_url, json=body)

        return request.text
    except Exception as e:
        print("sending exception :"+str(e))

    return None

def init():
    send_http_request("GET","/","")
