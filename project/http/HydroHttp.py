from project.Runtime import Runtime
from aiohttp import web, WSCloseCode

class HydroHttp(web.View):
    async def get(self):
        if self.request.path == "/": 
            return web.Response(text=self.load_file("web/index.html"), content_type="text/html", status=200)
        else:
            return web.Response(text=self.load_file("web/" + self.request.path), content_type="text/css", status=200)
            #     if 'favicon.ico' in self.path:
            #         self.send_response(404)
            #         return
            # filePath = path.replace("/css/", "web/")
            # return web.Response(text=self.load_file(self.request.path))

    # dispatch commands from mobile
    async def post(self):
        # c/play/[volume]
        # n/note
        splits = self.path.split('/')
        print(self.path)
        Runtime.get_engine().handleMessage(splits)
        self.send_response(200)
        self.end_headers()        

    # serve http requests - index.html
    def load_file(self, path):
        filePath = "web/index.html"

        f = open(filePath, "r")
        data = f.read()
        f.close()
        return data

