using System;
using System.Net;
using System.Net.Sockets;
using System.Threading.Tasks;
using TankioServer.HTTP;
using TankioServer.Client;
using System.IO;

namespace TankioServer.Listeners
{
    class TCPListener
    {
        TcpListener server;
        int port = 5005;

        bool waitingResponse = false;

        public void Init()
        {
            server = new TcpListener(IPAddress.Any, port);

            server.Start(80);   // and start the server
        }

        public void StartListener()
        {
            Task t = new Task(() => Listener());

            t.Start();
        }

        void ConnectionCallback(IAsyncResult result)
        {
            try
            {
                waitingResponse = false;

                TcpClient client = server.EndAcceptTcpClient(result);

                NetworkStream stream = client.GetStream();

                HttpRequest request = HttpRequest.FromStream(stream);

                HttpResponse response = TCPHandler.ProcessRequest(request);

                response.WriteToStream(stream);

                stream.Close();

                client.Close();

            }catch(Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }

        void Listener()
        {
            while (true)
            {
                while (waitingResponse) { }

                try
                {
                    server.BeginAcceptTcpClient(ConnectionCallback, null);
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.ToString());
                }
                waitingResponse = true;
            }
        }
    }
}
