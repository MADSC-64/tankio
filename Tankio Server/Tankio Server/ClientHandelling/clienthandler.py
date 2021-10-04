import threading
import Http.httpEncoder as encoder
import Http.httpDecoder as decoder
import ClientHandelling.clientRequester as requester

BUFFER_SIZE = 2048

def handle_TCP_client(conn):
    try:
        data = conn.recv(BUFFER_SIZE)

        if len(data) == 0:
            return

        response = requester.perform_request(data.decode('utf-8'))

        conn.send(bytes(response, 'utf-8'))  # echo
    except Exception as ex:
        print(ex)


def create_TCP_client_handler(conn):
    handler = threading.Thread(target=handle_TCP_client,args=(conn,))
    handler.start()