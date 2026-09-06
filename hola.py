import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 8000))
# Cambiar al directorio dist generado por flet publish
web_dir = os.path.join(os.path.dirname(__file__), "dist")
os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor Web corriendo en el puerto {PORT}")
    httpd.serve_forever()