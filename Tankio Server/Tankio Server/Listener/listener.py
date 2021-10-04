import ClientHandelling.clienthandler as client
import threading



def listener_thread_TCP(server):
    print("Thread TCP: starting")

    while 1:
        conn, addr = server.accept()
        client.create_TCP_client_handler(conn)

def listener_thread_UDP(server):
    print("Thread UDP: starting")

    while 1:
        data, addr = server.recvfrom(1024) # buffer size is 1024 bytes
        print("received message: %s" % data)


def start_listener_TCP(server):
    listener = threading.Thread(target=listener_thread_TCP,args=(server,))
    listener.start()

def start_listener_UDP(server):
    listener = threading.Thread(target=listener_thread_UDP,args=(server,))
    listener.start()

