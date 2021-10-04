import threading
import Http.httpEncoder as encoder
import Http.httpDecoder as decoder
import ClientHandelling.clientRequester as requester

BUFFER_SIZE = 2048

def handle_TCP_client(conn):
    data = conn.recv(BUFFER_SIZE)

    if len(data) == 0:
        return

    decoder.decodeHttpMessage(bytes.decode(data))

    response = encoder.generate_Http_response("200 OK","test")

    conn.send(bytes(response, 'utf-8'))  # echo


def create_TCP_client_handler(conn):
    handler = threading.Thread(target=handle_TCP_client,args=(conn,))
    handler.start()