import threading
from project.Config import Config
from aiohttp import web, WSCloseCode
import asyncio
from project.http.HydroHttp import HydroHttp

def thread_function(loop):
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    # loop.


class HydroServer():
    # create routes
    def create_runner(self):
        self.app = web.Application()
        self.app.add_routes([
            web.static('/', 'web'),
            web.post('/', HydroHttp),
            ## ,web.get('/ws', websocket_handler),
        ])
        return web.AppRunner(self.app)   

    async def start_server(self, host=Config.server_name(), port=Config.server_port()):
        self.runner = self.create_runner()
        await self.runner.setup()
        site = web.TCPSite(self.runner, host, port)
        await site.start()             

    # start http + wss server
    def start_serve(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.start_server())
        self.serverThread = threading.Thread(target=thread_function, args=[loop])
        self.serverThread.start()

    def quit(self):
        self.runner.shutdown()
        self.app.shutdown()
        self.serverThread.kill()
