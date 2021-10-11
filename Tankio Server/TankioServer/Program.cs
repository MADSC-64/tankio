using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TankioServer
{
    class Program
    {
        public static Listeners.TCPListener listenerTCP;

        static void Main(string[] args)
        {
            listenerTCP = new Listeners.TCPListener();
            listenerTCP.Init();
            listenerTCP.StartListener();

            while (true) { }

        }
    }
}
