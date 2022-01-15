from http.server import BaseHTTPRequestHandler
from project.engines.osc import OSCEngine

class HydroHttpServer(BaseHTTPRequestHandler):
    engine = OSCEngine()

    def do_GET(self):
        if 'favicon.ico' in self.path:
            self.send_response(404)
            return

        ## self.engine = OSCEngine()

        self.send_response(200)
        self.end_headers()
        self.wfile.write(self.loadFile())

    # dispatch commands from mobile
    def do_POST(self):
        splits = self.path.split('/')
        print(self.path)
        self.engine.executeCommand(splits)
        self.send_response(200)
        self.end_headers()


    # serve http requests - index.html
    def loadFile(self):
        if self.path == "/": 
            self.send_header("Content-type", "text/html")
            filePath = "web/index.html"
        else:
            self.send_header("Content-type", "text/css")
            filePath = self.path.replace("/css/", "web/")

        f = open(filePath, "r")
        return bytes(f.read(), "utf-8")
