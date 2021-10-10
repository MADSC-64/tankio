import Networking.networking as networking
import Networking.roomNetworking as rooms
import GameLogic.gameLogic as game
#import Rendering.gameRenderer as renderer

print(rooms.create_room("test"))

print(rooms.get_room_player_data(input("room id"),"test"))