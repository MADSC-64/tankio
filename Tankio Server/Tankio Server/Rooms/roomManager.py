import random


activeRooms = []

def getRandomRoom():
    activeRooms[0]

def createRoomToken(name):
    token = 0

    token = random.randint(10000,99999)

    while getRoomFromToken(token):
        token = random.randint(10000,99999)


    activeRooms.append((token,"test password",[name]))

    return token


def getRoomFromToken(token):

    for i in activeRooms:
        id, psw, players = i

        if id == int(token):
            return i

    return False

def joinRoom(token,name):
    room = getRoomFromToken(token)

    if room == False:
        return False

    id, psw, players = room

    players.append(name)

    return True