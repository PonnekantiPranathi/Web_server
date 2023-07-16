import http.server
import socketserver

PORT = 9090

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("",PORT),Handler)


print("Server is running ", PORT)
httpd.serve_forever()