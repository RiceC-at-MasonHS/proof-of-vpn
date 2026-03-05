import http.server
import socketserver
import socket
import os
import ipaddress
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

    def get_network_status(self, client_ip):
        try:
            ip_obj = ipaddress.ip_address(client_ip)
            if ip_obj.is_private:
                return "Local Network (RFC 1918)"
            if ip_obj.is_loopback:
                return "Local Loopback"
            return "Public / Remote Network"
        except ValueError:
            return "Unknown"

    def do_GET(self):
        server_ip = self.get_server_ip()
        client_ip = self.client_address[0]
        host_header = self.headers.get('Host', 'Unknown')
        network_status = self.get_network_status(client_ip)
        user_agent = self.headers.get('User-Agent', 'Unknown')

        if 'curl' in user_agent.lower():
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            response = f"""
+-------------------------------------------------+
|                                                 |
|          ~ Proof of Network Membership ~        |
|                                                 |
+-------------------------------------------------+

[ Server Information ]
Served From IP: {server_ip}
Host Header:    {host_header}

[ Client Information ]
Your IP Address: {client_ip}
Network Status:  {network_status}
User-Agent:      {user_agent}

[ Verdict ]
You are connecting via a {network_status} connection.
"""
            self.wfile.write(response.encode('utf-8'))
        elif self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            template = env.get_template('index.html')
            rendered_html = template.render(
                server_ip=server_ip,
                client_ip=client_ip,
                host_header=host_header,
                network_status=network_status,
                user_agent=user_agent
            )
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
