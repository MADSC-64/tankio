# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import Rooms.RoomManager as rooms
import json
import time
import platform



hostName = ""
serverPort = 5005

class MyServer(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _get_body(self):
        content_len = int(self.headers['content-length'])
        post_body = self.rfile.read(content_len)

        return post_body

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            f = open("HTML/icon.html", 'rb')
            self.wfile.write(f.read())
        elif self.path == "/favicon.ico":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            f = open("HTML/favicon.ico", 'rb')
            self.wfile.write(f.read())
        elif self.path == "/rest/players":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            response = str(rooms.get_global_players())

            self.wfile.write(bytes(response, "utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>404</title></head>", "utf-8"))
            self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>404 ERROR</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self):
        if self.path == "/rest/players/connect":
            self._set_response()

            data = json.loads( self._get_body().decode("utf-8"))
            response = str( rooms.player_connect(data["name"]))

            print(response)

            self.wfile.write(bytes(response, "utf-8"))


        elif self.path == "/rest/players/disconect":
            self._set_response()

            data = json.loads( self._get_body().decode("utf-8"))
            response = str( rooms.player_disconnect(data["name"],data["id"]))

            print(response)

            self.wfile.write(bytes(response, "utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>404</title></head>", "utf-8"))
            self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>404 ERROR</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")





