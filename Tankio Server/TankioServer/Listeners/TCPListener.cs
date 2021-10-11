using System;
using System.Net;
using System.IO;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace TankioServer.Listeners
{
    class TCPListener
    {
        HttpListener server;

        public void Init()
        {
            server = new HttpListener();  // this is the http server
            server.Prefixes.Add("http://127.0.0.1:5005/");  //we set a listening address here (localhost)
            server.Prefixes.Add("http://localhost:5005/");

            server.Start();   // and start the server
        }

        public void StartListener()
        {
            Task t = new Task(() => Listener());

            t.Start();
        }

        void ConnectionCallback(IAsyncResult result)
        {
            HttpListenerContext context = server.EndGetContext(result);
            //context: provides access to httplistener's response

            HttpListenerResponse response = context.Response;
            //the response tells the server where to send the datas

            string page = Directory.GetCurrentDirectory() + "/HTML" + context.Request.Url.LocalPath;
            //this will get the page requested by the browser 


            if (context.Request.Url.LocalPath == "/")  //if there's no page, we'll say it's index.html
                page += "index.html";


            Console.WriteLine(page);

            TextReader tr = new StreamReader(page);
            string msg = tr.ReadToEnd();  //getting the page's content

            byte[] buffer = Encoding.UTF8.GetBytes(msg);
            //then we transform it into a byte array

            response.ContentLength64 = buffer.Length;  // set up the messasge's length
            Stream st = response.OutputStream;  // here we create a stream to send the message
            st.Write(buffer, 0, buffer.Length); // and this will send all the content to the browser

            context.Response.Close();  // here we close the connection
        }

        void Listener()
        {
            while (true)
            {
                server.BeginGetContext(ConnectionCallback, null);
            }
        }
    }
}
