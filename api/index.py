from http.server import BaseHTTPRequestHandler
import json
import os # Jangan lupa import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Mengambil kunci dari Environment Variable Vercel
        RAHASIA_DARI_VERCEL = os.environ.get('KEY') 
        
        # Mengambil kunci yang dikirim oleh bot/user
        key_pengguna = self.headers.get("X-API-KEY")
        
        # Pengecekan
        if key_pengguna != RAHASIA_DARI_VERCEL:
            self.send_error(403, "Akses ditolak!")
            return

        # Jika sukses, kirim data
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        data = {"status": "success", "pesan": "Kunci benar, akses diberikan!"}
        self.wfile.write(json.dumps(data).encode())
        return
        
