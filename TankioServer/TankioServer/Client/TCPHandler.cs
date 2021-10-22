using System;
using System.IO;
using TankioServer.HTTP;
using TankioServer.Rooms;
using Newtonsoft.Json;

namespace TankioServer.Client
{
    class TCPHandler
    {
        public static HttpResponse ProcessRequest(HttpRequest request)
        {
            if(request == null) return HttpErrors.GenerateHttpError(404);

            if (request.method == "GET")
                return ProcessGetRequests(request);
            if (request.method == "POST")
                return ProcessPostRequests(request);

            return HttpErrors.GenerateHttpError(404);
        }

        public static HttpResponse ProcessGetRequests(HttpRequest request)
        {
            try
            {

                string path = request.path.LocalPath;

                HttpResponse response;

                switch (path)
                {
                    case "/":
                        response = new HttpResponse("tankio", 200, "text/html");
                        response.AddFile(Path.Join(AppDomain.CurrentDomain.BaseDirectory, "HTML/index.html"));

                        return response;

                    case "/favicon.ico":
                        response = new HttpResponse("tankio", 200, "image/vnd.microsoft.icon");
                        response.AddFile(Path.Join(AppDomain.CurrentDomain.BaseDirectory, "HTML/favicon.ico"));

                        return response;

                    case "/rest/players":
                        var players = RoomManager.registeredPlayers;

                        string data = JsonConvert.SerializeObject(players,Formatting.Indented);

                        return createDataResponse(data);

                    case "/rest/room":
                        var rooms = RoomManager.activeRooms;

                        string msg = JsonConvert.SerializeObject(rooms, Formatting.Indented);

                        return createDataResponse(msg);


                    default:
                        return HttpErrors.GenerateHttpError(404);

                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
                return HttpErrors.GenerateHttpError(500);
            }
        }

        public static HttpResponse ProcessPostRequests(HttpRequest request)
        {
            try
            {

                string path = request.path.LocalPath;

                Console.WriteLine(request.data);

                switch (path)
                {

                    case "/rest/create/room":
                        Player playerData = JsonConvert.DeserializeObject<Player>(request.data);

                        Room room = RoomManager.CreateRoom(playerData.name, playerData.id);

                        string msg = JsonConvert.SerializeObject(room);

                        return createDataResponse(msg);

                    case "/rest/create/player":
                        playerData = JsonConvert.DeserializeObject<Player>(request.data);

                        playerData = RoomManager.RegisterPlayer(playerData.name);

                        msg = JsonConvert.SerializeObject(playerData);

                        return createDataResponse(msg);
                }

                if (path.StartsWith("/rest/join/room/"))
                {

                    string roomIdString = path.Remove(0, 16);

                    int roomId = int.Parse(roomIdString);
                    Player playerData = JsonConvert.DeserializeObject<Player>(request.data);

                    Room room = RoomManager.JoinRoom(playerData.name, playerData.id, roomId);

                    string msg = JsonConvert.SerializeObject(room);

                    return createDataResponse(msg);
                }

            }
            catch(Exception e)
            {
                Console.WriteLine(e);
                return HttpErrors.GenerateHttpError(500);
            }

            return HttpErrors.GenerateHttpError(500);
        }

        public static HttpResponse createDataResponse(string data)
        {
            HttpResponse response;

            if (data == null ||  string.IsNullOrWhiteSpace(data) || string.IsNullOrEmpty(data) || data=="null")
            {
                return HttpErrors.GenerateHttpError(500);
            }

            response = new HttpResponse("tankio", 200, "text/text");

            response.AddString(data);

            return response;
        }
    }
}
