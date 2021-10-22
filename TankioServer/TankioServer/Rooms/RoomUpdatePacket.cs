namespace TankioServer.Rooms
{
    class RoomUpdatePacket
    {
        public Player player;
        public int id;
        public string requestType;
        public string requestName;
        public bool requestOverride;
        public long timestamp;

        public object data;
    }
}
