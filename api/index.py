from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Contoh data yang akan dikirim ke aplikasi lain
        data = {
            "status": "success",
            "pesan": "Halo! API ini sekarang berjalan di Vercel.",
            "data": [{"id": 1, "nama": "Contoh Data"}]
        }
        
        self.wfile.write(json.dumps(data).encode())
        return
      
