using System;

namespace TankioServer.Client
{
    class Time
    {
        public static long GetCurrentTimeStamp()
        {
            long timestamp = DateTime.Now.ToFileTimeUtc();

            return timestamp;
        }
    }
}
