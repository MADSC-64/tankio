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

    if len(activeRooms) == 0:
        return False

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

def joinRandomRoom(name):
    if len(activeRooms) == 0:
        createRoomToken(name)
        return

    randomIndex = random.randint(0,len(activeRooms))

    token, psw, players = activeRooms[randomIndex]

    joinRoom(token,name)
