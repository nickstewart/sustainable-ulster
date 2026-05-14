#!/usr/bin/env python3
import http.server, socketserver

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

with socketserver.TCPServer(("", 8000), Handler) as httpd:
    print("Serving at http://localhost:8000")
    httpd.serve_forever()
