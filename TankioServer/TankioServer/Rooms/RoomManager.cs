using System;
using System.Collections.Generic;
using TankioServer.Client;

namespace TankioServer.Rooms
{
    class RoomManager
    {
        public static List<Room> activeRooms = new List<Room>();
        public static List<Player> registeredPlayers = new List<Player>();

        static Random rng = new Random();


        public static Player RegisterPlayer(string name)
        {
            if (registeredPlayers.Count == 0)
            {
                int randomId = rng.Next(10000, 99999);
                Player player = new Player(name, randomId);

                registeredPlayers.Add(player);
                return player;
            }

            while (true)
            {
                int randomId = rng.Next(10000, 99999);

                if(!registeredPlayers.Contains(new Player(name, randomId)))
                {
                    Player player = new Player(name, randomId);

                    registeredPlayers.Add(player);
                    return player;
                }
            }
        }

        public static Player GetRegisteredPlayer(string name,int id)
        {
            if (registeredPlayers.Count == 0)
                return null;

            return registeredPlayers.Find(x => x.name == name && x.id == id);
        }   

        public static Room CreateRoom(string name, int id)
        {
            if (registeredPlayers.Count == 0)
                return null;

            Player player = GetRegisteredPlayer(name,id);
            if (player == null) return null;

            if (activeRooms.Count == 0)
            {
                int randomId = rng.Next(10000, 99999);
                Room room = new Room(randomId, "test");

                room.players.Add(player);

                room.roomEvents.Add(("room", 0), new List<Event> { new Event(Time.GetCurrentTimeStamp(), "created", null) });
                room.roomEvents.Add((name, id), new List<Event> { new Event(Time.GetCurrentTimeStamp(), "joined", null) });

                activeRooms.Add(room);

                return room;
            }

            while (true)
            {
                int randomId = rng.Next(10000, 99999);

                if(!activeRooms.Exists(x => x.id == randomId))
                {
                    Room room = new Room(randomId, "test");

                    room.players.Add(player);

                    room.roomEvents.Add(("room", 0), new List<Event> { new Event(Time.GetCurrentTimeStamp(), "created", null) });
                    room.roomEvents.Add((name, id), new List<Event> { new Event(Time.GetCurrentTimeStamp(), "joined", null) });

                    activeRooms.Add(room);

                    return room;
                }
            }
        }

        public static Room JoinRoom(string name, int id,int roomID)
        {
            if (registeredPlayers.Count == 0)
                return null;

            Player player = GetRegisteredPlayer(name, id);

            if (player == null) return null;

            if (activeRooms.Count == 0)
            {
                return null;
            }

            Room targetRoom = activeRooms.Find(x => x.id == roomID);

            if (targetRoom == null) return null;

            if( targetRoom.roomEvents[("room", 0)].Exists(x => x.eventName == "started"))
                return null;

            targetRoom.players.Add(player);

            if (!targetRoom.roomEvents.ContainsKey((name, id)))
                targetRoom.roomEvents.Add((name, id), new List<Event> { new Event(Time.GetCurrentTimeStamp(), "joined", null) });

            return targetRoom;
        }

        public static Room GetRoomData(string name,int id,int roomID)
        {
            if (registeredPlayers.Count == 0)
                return null;

            Player player = GetRegisteredPlayer(name, id);

            if (player == null) return null;

            if (activeRooms.Count == 0)
            {
                return null;
            }

            return activeRooms.Find(x => x.id == roomID);
        }

        public static void UpdateRoomPlayerData(string name, int id, int roomID, string eventName, bool overrideData, object data)
        {
            if (registeredPlayers.Count == 0)
                return;

            Player player = GetRegisteredPlayer(name, id);

            if (player == null) return;

            if (activeRooms.Count == 0)
            {
                return;
            }

            Room targetRoom = activeRooms.Find(x => x.id == roomID);

            if (targetRoom == null) return;

            Event roomEvent = new Event(Time.GetCurrentTimeStamp(), eventName, data);

            if (overrideData)
            {
                int targetEventIndex = targetRoom.roomEvents[(name, id)].FindIndex(x => x.eventName == eventName);

                if(targetEventIndex <= 0)
                {
                    targetRoom.roomEvents[(name, id)].Add(roomEvent);
                    return;
                }

                targetRoom.roomEvents[(name, id)][targetEventIndex] = roomEvent;

                return;
            }

            targetRoom.roomEvents[(name, id)].Add(roomEvent);

            return;
        }

        public static Room UpdateRoomData(string name, int id, int roomID,string eventName,bool overrideData,object data)
        {
            if (registeredPlayers.Count == 0)
                return null;

            Player player = GetRegisteredPlayer(name, id);

            if (player == null) return null;

            if (activeRooms.Count == 0)
            {
                return null;
            }

            Room targetRoom = activeRooms.Find(x => x.id == roomID);

            if (targetRoom == null) return null;

            Event roomEvent = new Event(Time.GetCurrentTimeStamp(), eventName, data);

            if (overrideData)
            {
                int targetEventIndex = targetRoom.roomEvents[("room", 0)].FindIndex(x => x.eventName == eventName);

                targetRoom.roomEvents[("room", 0)][targetEventIndex] = roomEvent;

                return targetRoom;
            }

            targetRoom.roomEvents[("room", 0)].Add(roomEvent);

            return targetRoom;
        }

    }
}
