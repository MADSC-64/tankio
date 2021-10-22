using System;
using System.Collections.Generic;
using System.IO;

namespace TankioServer.HTTP
{
    public class HttpRequest : HttpBase
    {
        public Uri path;
        public string method;
        public string data;

        //---------------------Decoding---------------------------
        public static HttpRequest FromStream(Stream stream)
        {
            try
            {

                if (stream == null) return null;

                StreamReader reader = new StreamReader(stream);

                //Gets All Path And Method Info From Request Line
                DecodeRequestLine(reader, out string method, out string path);

                //Gets All Pressent Headers
                var headers = GetHeaders(reader);

                //Gets Http Request Data
                var data = GetData(reader);

                //Gets Full Request Url
                Uri requestPath = UrlProcessing.GetAbsoluteUrl(path, headers);

                var queryParams = GetQueryParameters(requestPath);

                return new HttpRequest(requestPath, method, headers, queryParams, data);
            }
            catch (Exception e)
            {
                return null;
            }
        }

        static void DecodeRequestLine(StreamReader reader, out string method, out string path)
        {
            method = "";
            path = "";

            try
            {
                string requestLine = reader.ReadLine();

                if (requestLine == null) return;

                string[] requestLineTokens = requestLine.Split(' ');

                method = requestLineTokens[0];
                path = requestLineTokens[1];
            }
            catch (Exception e)
            {
                
            }
        }

        static string GetData(StreamReader reader)
        {
            string data = "";

            while (reader.Peek() >= 0)
            {
                data += (char)reader.Read();
            }

            return data;
        }

        //---------------------Encoding---------------------------
        string GenerateHttpHeaders()
        {
            //Creates And Adds Request Line
            string httpStringData = $"{method} {path} HTTP/1.1\nHost: MADSC SERVER\n";

            //If Present Adds Headers
            httpStringData += HeadersToString();

            return httpStringData;
        }

        public void WriteToStream(Stream stream)
        {
            string httpHeaders = GenerateHttpHeaders();

            WriteHttpHeadersToStream(httpHeaders, stream);
        }
        //---------------------Constructors-----------------------

        public HttpRequest(Uri path, string method, Dictionary<string, string> headers, Dictionary<string, string> queryParameters, string data)
        {
            this.path = path;
            this.method = method;
            this.headers = headers;
            this.queryParameters = queryParameters;
            this.data = data;
        }

    }
}
