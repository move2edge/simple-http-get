import http.server
import socketserver

PORT = 80


class Handler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        with open("data.txt", 'r') as file:
            self.wfile.write(file.read().strip().encode("utf8"))

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
