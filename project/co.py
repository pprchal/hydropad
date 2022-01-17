from aiohttp import web
from threading import Thread


class Handler:
    def __init__(self):
        pass


    async def handle_intro(self, request):
        return web.Response(text="Hello, world")

    async def handle_greeting(self, request):
        name = request.match_info.get('name', "Anonymous")
        txt = "Hello, {}".format(name)
        return web.Response(text=txt)
 

class ServerThread(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.app = web.Application()
        handler = Handler()

        self.app.add_routes([
            web.get('/', handler.handle_intro),
            web.get('/greet/{name}', handler.handle_greeting)])

    def run(self):
        web.run_app(self.app)

 

t = ServerThread()

t.start()

print("<ENTER>")

input()