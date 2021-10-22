using System.Collections.Generic;

namespace TankioServer.Rooms
{
    class Room
    {
        public int id;
        public string name;

        public List<Player> players = new List<Player>();
        public Dictionary<(string, int), List<Event>> roomEvents = new Dictionary<(string, int), List<Event>>();

        public Room(int id,string name)
        {
            this.id = id;
            this.name = name;
        }
    }

    class Event
    {
        public long timestamp;
        public string eventName;
        public object eventValue;

        public Event(long timestamp, string eventName, object eventValue)
        {
            this.timestamp = timestamp;
            this.eventName = eventName;
            this.eventValue = eventValue;
        }
    }
}


