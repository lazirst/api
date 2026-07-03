from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Kirim status sukses
        self.send_response(200)
        
        # 2. Set header agar browser tahu ini data JSON
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # 3. Data yang mau dikirim
        data = {
        "status" : "success connect API"
        "data_info" : [
        {"id" : 1, "nama" : "dani", "umur" : 29}
        {"id" : 2, "nama" : "bacok", "umur" : 24}
        ]
        }
        
        # 4. Kirim datanya
        self.wfile.write(json.dumps(data).encode())
        return

