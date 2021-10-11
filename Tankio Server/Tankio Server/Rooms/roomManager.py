from .room import room
import random as rng
import datetime
import json

active_rooms = []
global_players = []


# Player Managment

def get_global_players():
    list = [{"name": x[0], "id": x[1], "connection_timestamp": x[2]} for x in global_players]
    
    return list

def player_connect(name):
    while 1:
        ts = datetime.datetime.now().timestamp()
        player_id = rng.randint(100000,999999)

        if (name,player_id) not in global_players:
            global_players.append((name,player_id,ts))
            return {'state':'conected','name':name,'id':player_id,'timestamp':ts}

def player_disconnect(name,id):
    ts = datetime.datetime.now().timestamp()

    for player in global_players:
        if player[0] == name and int(player[1]) == id:
            global_players.remove(player)

            return {'state':'disconected','name':name,'id':id,'timestamp':ts}
    return {"state":"ERROR disconected player doesnt exist",'name':name,'id':id,'timestamp':ts}

# 