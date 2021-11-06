using Newtonsoft.Json;
using System;

namespace TankioServer.Client
{
    class UDPHandler
    {
        public static string ProcessRequest(string msg)
        {
            try
            {
                Rooms.RoomUpdatePacket roomUpdate = JsonConvert.DeserializeObject<Rooms.RoomUpdatePacket>(msg);

                int playerID = roomUpdate.player.id;
                int roomID = roomUpdate.id;
                string playerName = roomUpdate.player.name;
                string requestType = roomUpdate.requestType;
                string dataName = roomUpdate.requestName;
                bool dataOverride = roomUpdate.requestOverride;
                object data = roomUpdate.data;

                Rooms.Player player = Rooms.RoomManager.GetRegisteredPlayer(playerName, playerID);

                if(player == null) return (@"{""type"": ""ERROR"",""message"": ""PLAYER MISSING ERROR""}");

                Console.WriteLine(requestType);
                Console.WriteLine(requestType.StartsWith("POST"));

                if (requestType.StartsWith("POST",StringComparison.CurrentCultureIgnoreCase))
                {
                    requestType = requestType.Remove(0, 5);

                    switch (requestType)
                    {
                        case "ROOM":
                            return JsonConvert.SerializeObject(Rooms.RoomManager.UpdateRoomData(playerName, playerID, roomID, dataName, dataOverride, data));

                        case "PLAYER":
                            return JsonConvert.SerializeObject(Rooms.RoomManager.UpdateRoomPlayerData(playerName, playerID, roomID, dataName, dataOverride, data));
                        default:
                            return (@"{""type"": ""ERROR"",""message"": ""POST PROCESSING ERROR""}");
                    }
                }

                if (requestType.StartsWith("GET", StringComparison.CurrentCultureIgnoreCase))
                {
                    requestType = requestType.Remove(0, 4);

                    switch (requestType)
                    {
                        case "ROOM":
                            return JsonConvert.SerializeObject(Rooms.RoomManager.GetRoomData(playerName, playerID, roomID));

                        default:
                            return (@"{""type"": ""ERROR"",""message"": ""GET PROCESSING ERROR""}");
                    }
                }
            }
            catch (Exception e) {
                Console.WriteLine(e);
            }

            return (@"{""type"": ""ERROR"",""message"": ""UDP PROCESSING ERROR""}");
        }
    }
}
