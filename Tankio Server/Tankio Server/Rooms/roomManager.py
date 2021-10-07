import random


activeRooms = []

def getRandomRoom():
    activeRooms[0]

def createRoomToken(name):
    token = 0

    token = random.randint(10000,99999)

    while getRoomFromToken(token):
        token = random.randint(10000,99999)


    activeRooms.append((token,"test password",[name],[]))

    return token


def getRoomFromToken(token):

    if len(activeRooms) == 0:
        return False

    for i in activeRooms:
        id, psw, players,data = i

        if id == int(token):
            return i

    return False

def joinRoom(token,name):
    room = getRoomFromToken(token)

    if room == False:
        return False

    id, psw, players,data = room

    players.append(name)

    return True

def joinRandomRoom(name):
    if len(activeRooms) == 0:
        createRoomToken(name)
        return

    randomIndex = random.randint(0,len(activeRooms))

    id, psw, players,data = activeRooms[randomIndex]

    joinRoom(token,name)

# Player Room Data

def UpdatePlayerData(name,old_data,new_data):
    for i in old_data:
        player_name, pos_x,pos_y,is_alive,last_fire_time = i

        if player_name == name:
            i = new_data
            return old_data

def getRoomData(token):
    room = getRoomFromToken(token)

    if room == False:
        return False

    id, psw, players,data = room

    return data

def updateRoomPlayerData(token,name,new_data):
    room = getRoomFromToken(token)

    if room == False:
        return False

    id, psw, players,data = room

    data = UpdatePlayerData(name,data,new_data)

def updateRoomPlayerData(token,name,new_data):
    room = getRoomFromToken(token)

    if room == False:
        return False

    id, psw, players,data = room

    data = UpdatePlayerData(name,data,new_data)