import ClientHandelling.clienthandler as client
import threading



def listener_thread_TCP(server):
    print("Thread: starting")

    while 1:
        conn, addr = server.accept()
        client.create_TCP_client_handler(conn)


def start_listener_TCP(server):
    listener = threading.Thread(target=listener_thread_TCP,args=(server,))
    listener.start()