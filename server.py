import http.server
import socketserver
import os

TARGET_DIR = r"E:\localhost\website"

if os.path.exists(TARGET_DIR):
    os.chdir(TARGET_DIR)
else:
    print(f"Error: Could not find folder {TARGET_DIR}")

PORT = 8000

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def do_GET(self):
        # Force the server to load index.html immediately instead of showing a directory list
        if self.path == '/' or self.path == '':
            self.path = '/index.html'
        return super().do_GET()

socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), NoCacheHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    print(f"Serving files from: {os.getcwd()}")
    httpd.serve_forever()