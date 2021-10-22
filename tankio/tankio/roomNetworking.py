import networking
import json

def create_player(name):
    content = {'name':name,'id':0}

    print(content)

    result = networking.send_http_request("POST","/rest/create/player",content)

    print(json.loads(result))


    return json.loads(result)

def join_room(token,name,id):
    content = {'name':name,'id':id}

    print(content)

    result = networking.send_http_request("POST",f"/rest/join/room/{token}",content)

    return json.loads(result)

def get_room_data(token,name,id):
    content = { "player":{"name":name,"id":id},  "id":token, "requestType": "GET/ROOM", "requestName": "","requestOverride":true,"timestamp": 0,"data": null}

    return networking.send_recieve_to_server_UDP(content)

def create_room(name,id):
    content = {'name':name,'id':id}

    result = networking.send_http_request("POST","/rest/create/room",content)

    return json.loads(result)

