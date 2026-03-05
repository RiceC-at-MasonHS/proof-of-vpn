import http.server
import socketserver
import socket
import os
from jinja2 import Environment, FileSystemLoader

PORT = 8000

# Setup Jinja2 environment
TEMPLATE_DIR = os.path.dirname(os.path.abspath(__file__))
loader = FileSystemLoader(TEMPLATE_DIR)
env = Environment(loader=loader)

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def get_server_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    def do_GET(self):
        if 'curl' in self.headers.get('User-Agent', ''):
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            IP = self.get_server_ip()

            response = f"""
+-------------------------------------------------+
|                                                 |
|          ~ Proof of Network Membership ~        |
|                                                 |
+-------------------------------------------------+

This server is responding from: {IP}
"""
            self.wfile.write(response.encode('utf-8'))
        elif self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            template = env.get_template('index.html')
            IP = self.get_server_ip()
            rendered_html = template.render(server_ip=IP)
            self.wfile.write(rendered_html.encode('utf-8'))
        elif self.path == '/404.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            with open('404.html', 'rb') as f:
                self.wfile.write(f.read())
        else:
            # Serve other static files
            super().do_GET()

with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
