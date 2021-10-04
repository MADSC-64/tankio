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
