import json
import time
import platform
import roomNetworking

player = roomNetworking.create_player("test")

print(player["name"]," ",player["id"])

print(roomNetworking.create_room(player["name"],player["id"]))

import gameRenderer
