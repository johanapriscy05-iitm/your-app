import json
import os
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

# Get the absolute path of q-vercel-python.json
file_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")

# Read and load the JSON data
with open(file_path, "r") as f:
    marks_data = json.load(f)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query = parse_qs(self.path.split('?')[-1])
        names = query.get('name', [])

        # Fetch marks for requested names
        response = {"marks": [marks_data.get(name, 0) for name in names]}

        # Enable CORS
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        

        # Send response
        self.wfile.write(json.dumps(response).encode('utf-8'))
