from http.server import BaseHTTPRequestHandler
from osc import OSC

class HydroHttpServer(BaseHTTPRequestHandler):
    def __init__(self):
        self.oscClient = OSC()

    def do_GET(self):
        if 'favicon.ico' in self.path:
            self.send_response(404)
            return

        self.send_response(200)
        self.end_headers()
        self.wfile.write(self.loadFile())

    def loadFile(self):
        if self.path == "/": 
            self.send_header("Content-type", "text/html")
            filePath = "web/index.html"
        else:
            self.send_header("Content-type", "text/css")
            filePath = self.path.replace("/css/", "web/")

        f = open(filePath, "r")
        return bytes(f.read(), "utf-8")


    def do_POST(self):
        splits = self.path.split('/')
        print(self.path)
        
        if len(splits) == 3:
            command = splits[2].upper()
            self.oscClient.command(command, 1)
        elif len(splits) == 4:
            command = splits[2].upper()
            param = splits[3].upper()
            self.oscClient.command(command, param)

        self.send_response(200)
        self.end_headers()
        
        
        
        
    
