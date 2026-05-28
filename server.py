import http.server
import socketserver
import mimetypes

mimetypes.init()
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('text/html', '.html')

class Handler(http.server.SimpleHTTPRequestHandler):
    pass

PORT = 8080
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT} with fixed MIME types")
    httpd.serve_forever()
