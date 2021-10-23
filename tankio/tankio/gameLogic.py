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

        print(self.username," ",self.id)

    def createRoom(self):
        print(self.username)
        print(self.id)

        room = roomNetworking.create_room(self.username,self.id)
    
        self.token = room["id"]

        print(self.token )

    def getRoomData(self):
        return roomNetworking.get_room_data(self.token ,self.username,self.id)

    def joinRoom(self,token):
        print(self.username)
        print(self.id)

        room = roomNetworking.join_room(token,self.username,self.id)

        self.token = token

        if room == None:
            return None

        print(room)

