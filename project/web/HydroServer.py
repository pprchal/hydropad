from http.server import BaseHTTPRequestHandler
from project.engines.engine import AbstractEngine
from config import config

import aiohttp
from aiohttp import web, WSCloseCode
import asyncio


from HydroHttp import HydroHttpServer

class HydroServer():

    async def http_handler(self, request):
        return web.Response(text="hello")

    def create_runner(self):
        app = web.Application()
        app.add_routes([
            web.get('/', HydroHttpServer)
            ## ,web.get('/ws', websocket_handler),
        ])
        return web.AppRunner(app)   

    async def start_server(self, host=config.server_name(), port=config.server_port()):
        runner = self.create_runner()
        await runner.setup()
        site = web.TCPSite(runner, host, port)
        await site.start()             

    # start http + wss server
    def start(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.start_server())
        loop.run_forever()

    def thread_function(ws):
        try:
            ws.serve_forever()
        except KeyboardInterrupt:
            pass
        ws.server_close()


# app.webServer = HTTPServer((config.server_name(), config.server_port()), HydroHttpServer)
# app.httpThread = threading.Thread(target=thread_function, args=[app.webServer])
# app.httpThread.start()