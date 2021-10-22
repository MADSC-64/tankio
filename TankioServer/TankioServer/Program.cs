using System;

namespace TankioServer
{
    class Program
    {
        public static Listeners.TCPListener listenerTCP;
        public static Listeners.UDPListener listenerUDP;


        static void Main(string[] args)
        {
            Console.WriteLine("Starting TCP");

            listenerTCP = new Listeners.TCPListener();
            listenerTCP.Init();
            listenerTCP.StartListener();

            Console.WriteLine("Starting UDP");

            listenerUDP = new Listeners.UDPListener();
            listenerUDP.Init();
            listenerUDP.StartListener();

            Console.Beep();

            while (true) { }

        }
    }
}
