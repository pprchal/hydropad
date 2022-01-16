from aiohttp import web, WSCloseCode

class HydroHttpServer(web.View):
    async def get(self):
        return web.Response(text=self.load_file())

    # dispatch commands from mobile
    def do_POST(self):
        # c/play/[volume]
        # n/note
        splits = self.path.split('/')
        print(self.path)
        self.engine.handleMessage(splits)
        self.send_response(200)
        self.end_headers()        

    # serve http requests - index.html
    def load_file(self, path):
        if path == "/": 
            self.send_header("Content-type", "text/html")
            filePath = "web/index.html"
        else:
            self.send_header("Content-type", "text/css")
            filePath = path.replace("/css/", "web/")

        f = open(filePath, "r")
        data = f.read()
        f.close()
        return bytes(data, "utf-8")    

            # serve HTTP
    # def do_GET(self):
    #     if 'favicon.ico' in self.path:
    #         self.send_response(404)
    #         return

    #     self.send_response(200)
    #     self.end_headers()
    #     self.wfile.write(self.loadFile())