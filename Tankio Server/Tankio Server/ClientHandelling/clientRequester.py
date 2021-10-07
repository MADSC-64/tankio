import Http.httpDecoder as decoder
import Http.httpEncoder as encoder
import Rooms.roomManager as rooms
import json

def perform_UDP_request(request,addr):
    body = json.loads(request)

    return get_UDP_response(body,addr)



def perform_request(request):
    url,type,body = decoder.decodeHttpMessage(request)

    if not body.isspace() and len(body) != 0:
        body = json.loads(body)
        print("JSON")

    response_code, body = get_response(url,type,body)


    response = encoder.generate_Http_response(response_code,body)

    return response


def get_response(url,type,body):
    if type != "GET" and type != "POST":
        return ("405 Method Not Allowed","ERROR: 405 Method Not Allowed")

    if url == "/rest/players" and type == "GET":
        return ("200 OK","NOT IMPLEMENTED")

    if url == "/rest/room/create" and type == "POST":
        token = rooms.createRoomToken(body["name"])

        return ("200 OK",f"Created Token:{token} for player test")

    if url == "/rest/room" and type == "GET":
        return ("200 OK",str(rooms.activeRooms))

    if url == "/rest/room/join" and type == "POST":
        if rooms.joinRoom(body["token"],body["name"]):
            return ("200 OK","Joined Room")
            
        return ("500 Internal Server Error","Failed To Join")

    if url == "/rest/room/join/random" and type == "POST":
        rooms.joinRandomRoom(body["name"])
        return ("200 OK","Joined Room")
            



    return ("400 Bad Request","ERROR: 400 Bad Request")

def get_UDP_response(request,addr):
    token = int( request["token"])
    name = request["name"]
    body = request["body"]
    request_type = str( request["type"])

    print(name)
    print(token)
    print(body)
    print(request_type)

    if request_type == "POST/PLAYER":
        if rooms.getRoomFromToken(token) == False:
            return

        rooms.updateRoomPlayerData(token,name,body)

    if request_type == "GET":
        print("GET Method Started",rooms.getRoomFromToken(token))
        data = rooms.getRoomData(token)
        
        if data == False:
            return "ROOM ERROR"

        return data

    return "ERROR: METHOD NOT FOUND"

