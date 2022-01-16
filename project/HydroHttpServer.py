from http.server import BaseHTTPRequestHandler
from project.engines.engine import AbstractEngine
from config import config
from project.engines.osc import OSCEngine
from project.engines.midi import MIDIEngine

import aiohttp
from aiohttp import web, WSCloseCode
import asyncio


async def http_handler(request):
    return web.Response(text="hello")


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str('some websocket message payload')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' % ws.exception())

    return ws







class HydroHttpServer():
    # TODO: do better factory here
    if config.engine() == "OSC":
        engine = OSCEngine()
    else:
        engine = MIDIEngine()

    def create_runner(self):
        app = web.Application()
        app.add_routes([
            web.get('/', http_handler),
            web.get('/ws', websocket_handler),
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

        # if request.path == 'favicon.ico':
        #     return web.Response(status=404)

        # return web.Response(text=self.loadFile(request.path))

    # serve HTTP
    # def do_GET(self):
    #     if 'favicon.ico' in self.path:
    #         self.send_response(404)
    #         return

    #     self.send_response(200)
    #     self.end_headers()
    #     self.wfile.write(self.loadFile())

    # dispatch commands from mobile
    # def do_POST(self):
    #     # c/play/[volume]
    #     # n/note
    #     splits = self.path.split('/')
    #     print(self.path)
    #     self.engine.handleMessage(splits)
    #     self.send_response(200)
    #     self.end_headers()


    # serve http requests - index.html
    def loadFile(self, path):
        if path == "/": 
            self.send_header("Content-type", "text/html")
            filePath = "web/index.html"
        else:
            self.send_header("Content-type", "text/css")
            filePath = path.replace("/css/", "web/")

        f = open(filePath, "r")
        return bytes(f.read(), "utf-8")

    def thread_function(ws):
        try:
            ws.serve_forever()
        except KeyboardInterrupt:
            pass
        ws.server_close()


# app.webServer = HTTPServer((config.server_name(), config.server_port()), HydroHttpServer)
# app.httpThread = threading.Thread(target=thread_function, args=[app.webServer])
# app.httpThread.start()
