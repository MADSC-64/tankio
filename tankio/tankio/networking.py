import requests
import socket
import json

server_name = "http://server.wummo.eu:5005"
server_host = '212.117.19.158'
server_port_TCP = 5005
server_port_UDP = 5000

BUFFER_SIZE = 2048

socket_UDP = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
socket_UDP.bind(('', 5001))

def send_recieve_to_server_UDP(msg):
    try:
        msg = json.dumps(msg)

        socket_UDP.sendto(bytes(msg,'utf-8'),('212.117.19.158', 5000))
        socket_UDP.settimeout(2)

        data , addr = socket_UDP.recvfrom(1024)

        print(data)

        return json.loads(data)
    except socket.timeout:
        print("timeout")
        return None

def send_to_server_UDP(msg):
    try:
        msg = json.dumps(msg)

        socket_UDP.sendto(bytes(msg,'utf-8'),('212.117.19.158', 5000))
    except Exception as e:
        print("sending exception :"+str(e))



def send_http_request(method,target_url,body):
    try:
        request = None

        if method == "POST":
            request = requests.post(server_name+target_url, json=body)
            if request.status_code != 200:
                return None

        return request.text
    except Exception as e:
        print("sending exception :"+str(e))

    return None

def init():
    send_http_request("GET","/","")
