import json
from http.server import BaseHTTPRequestHandler
import urllib.parse

# Define the student marks dictionary with updated data
student_marks = [{"name":"LYxs","marks":58},{"name":"KmAOZuB5h","marks":45},{"name":"2EHyD3m","marks":67},{"name":"65ekYL","marks":0},{"name":"ec8HQ","marks":30},{"name":"38ZRV","marks":95},{"name":"aeuA","marks":10},{"name":"DFCC9Z","marks":8},{"name":"H0N0","marks":4},{"name":"f0MahL","marks":12},{"name":"I5ZQ6","marks":73},{"name":"eK","marks":60},{"name":"xx","marks":98},{"name":"rrMOHGKdz","marks":51},{"name":"RdgWED1mu2","marks":85},{"name":"PjITQM8R","marks":4},{"name":"sdqPy","marks":38},{"name":"rI","marks":73},{"name":"nlwI1","marks":62},{"name":"HiMQ","marks":35},{"name":"uQ","marks":51},{"name":"Yv84e3hS","marks":0},{"name":"0Yn2Z","marks":55},{"name":"4dsBfpL","marks":36},{"name":"F","marks":71},{"name":"RYCUm","marks":87},{"name":"JX","marks":49},{"name":"drQ4g6WPWG","marks":51},{"name":"mEUc306","marks":14},{"name":"uU0C32Y","marks":60},{"name":"QQoUK","marks":54},{"name":"1T","marks":5},{"name":"hFYx55AuN","marks":8},{"name":"j9g","marks":3},{"name":"1wR","marks":97},{"name":"5ONC","marks":93},{"name":"5K","marks":19},{"name":"X","marks":40},{"name":"gNUD2LYrc","marks":37},{"name":"HoR","marks":17},{"name":"m3N","marks":74},{"name":"Kn","marks":87},{"name":"ykU0YJSlmv","marks":84},{"name":"Ow","marks":3},{"name":"Qy","marks":59},{"name":"lYYE9","marks":29},{"name":"czY","marks":18},{"name":"tr","marks":0},{"name":"Txct","marks":23},{"name":"A0K","marks":12},{"name":"d","marks":64},{"name":"RHLnO","marks":13},{"name":"uu","marks":54},{"name":"PlJIuQ6waS","marks":96},{"name":"h1AKC","marks":79},{"name":"RAUZysmA8","marks":80},{"name":"ZecL1LJVo","marks":26},{"name":"y","marks":47},{"name":"5DpUveB3","marks":31},{"name":"F0ENb","marks":23},{"name":"YaXL","marks":53},{"name":"r","marks":5},{"name":"YmcCoZX1","marks":0},{"name":"AZahlo","marks":13},{"name":"8CbOiEezO","marks":0},{"name":"06G8nTz","marks":11},{"name":"y2id4","marks":83},{"name":"8yoduIN0","marks":71},{"name":"CWt7IjPtEn","marks":87},{"name":"1kaBRZ7m","marks":77},{"name":"55R8AZ","marks":50},{"name":"i1zHg8R4d","marks":40},{"name":"jqkxa6nEc","marks":77},{"name":"4ddH","marks":17},{"name":"4IHPsXh","marks":84},{"name":"Q","marks":1},{"name":"KCTir","marks":80},{"name":"XPx1","marks":28},{"name":"7iNI","marks":5},{"name":"kh","marks":37},{"name":"W6qE3","marks":70},{"name":"R4","marks":68},{"name":"cE","marks":78},{"name":"RTPhlUx","marks":90},{"name":"9cAZTjI","marks":96},{"name":"ZrM7go","marks":44},{"name":"K8qURF3DD","marks":97},{"name":"zzSmnTt","marks":74},{"name":"tNl0r1QFJ8","marks":91},{"name":"kQ","marks":25},{"name":"zIySbnat5H","marks":34},{"name":"bl22","marks":17},{"name":"ItloxTu","marks":96},{"name":"dAxmsGz","marks":45},{"name":"IaB43","marks":15},{"name":"TJ","marks":21},{"name":"RLjko","marks":19},{"name":"5ranyB","marks":44},{"name":"mV","marks":40},{"name":"wd9XqxiGgQ","marks":11}]

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the query parameters
        query_components = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        names = query_components.get("name", [])

        # Get the marks for each requested student
        marks = [
            next((student["marks"] for student in student_marks if student["name"] == name), "Not Found")
            for name in names
        ]

        # Create JSON response
        response = {"marks": marks}

        # Send HTTP response headers
        self.send_response(200)
        self.send_header("Content-type", "application/json")

        # Enable CORS (Allow all origins)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

        self.end_headers()

        # Send response body
        self.wfile.write(json.dumps(response).encode("utf-8"))

    def do_OPTIONS(self):
        # Handle preflight requests for CORS
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
