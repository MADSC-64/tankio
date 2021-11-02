import roomNetworking

class gameLogic:
    def __init__(self):
        super(gameLogic,self).__init__()
        self.username = ""
        self.id = 0
        self.token = 0

    def createUser(self,msg):

        player = roomNetworking.create_player(msg)
        self.username = player["name"]
        self.id = player["id"]
    def createRoom(self):
        room = roomNetworking.create_room(self.username,self.id)
    
        self.token = room["id"]

    def update_room_data(self,event_name,data):
        roomNetworking.update_room_data(self.token,self.username,self.id,data,event_name)

    def getRoomData(self):
        return roomNetworking.get_room_data(self.token ,self.username,self.id)

    def joinRoom(self,token):
        room = roomNetworking.join_room(token,self.username,self.id)

        print(room)

        self.token = token

        return room

