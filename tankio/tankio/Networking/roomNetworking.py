import Networking.networking as networking
import json

def join_room(token,name):
    content = json.dumps({'name':name,'token':token})

    print(content)

    result = networking.send_http_request("POST","/rest/room/join",content)

    print(result)


    if "Joined Room" in result:
        return True

    return False

def get_room_player_data(token,name):
    content = json.dumps({"type":"GET",'name':name,'token':token,'body':[]})

    return networking.send_recieve_to_server_UDP(content)

def create_room(name):
    content = json.dumps({'name':name})

    result = networking.send_http_request("POST","/rest/room/create",content)
