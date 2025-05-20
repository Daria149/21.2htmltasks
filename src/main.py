import os
from http.server import BaseHTTPRequestHandler, HTTPServer

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_ = os.path.join(project_path, "src", "contacts.html")

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        """Метод для обработки GET-запросов"""
        try:
            with open("contacts.html", "r", encoding="utf-8") as file:
                html_contacts = file.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(html_contacts, "utf-8"))
        except FileNotFoundError:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1>Error: 404 - Page Not Found</h1>")


    def do_POST(self):
        """Метод для обработки POST-запросов"""
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print(body)
        self.send_response(200)
        self.end_headers()



if __name__ == "__main__":
    webMyServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started at http://{hostName}:{serverPort}")

    try:
        webMyServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webMyServer.server_close()
    print("Server stopped.")
