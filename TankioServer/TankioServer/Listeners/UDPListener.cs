using System;
using System.Net;
using System.Net.Sockets;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using TankioServer.Client;

namespace TankioServer.Listeners
{
    class UDPListener
    {


        IPEndPoint server;
        int port = 5000;

        public void Init()
        {
            server = new IPEndPoint(IPAddress.Any, port);
        }

        public void StartListener()
        {
            Task t = new Task(() => Listener());

            t.Start();
        }

        void Listener()
        {
            UdpClient newsock = new UdpClient(server);

            Console.WriteLine("Waiting for a client...");

            IPEndPoint sender = new IPEndPoint(IPAddress.Any, 5001);

            byte[] data = new byte[1024];

            while (true)
            {
                try
                {
                    data = newsock.Receive(ref sender);

                    string request = Encoding.UTF8.GetString(data, 0, data.Length);

                    string response = UDPHandler.ProcessRequest(request);

                    byte[] responseData = Encoding.UTF8.GetBytes(response);

                    newsock.Send(responseData, responseData.Length,sender);
                }
                catch (Exception) { }
            }
        }
    }
}
