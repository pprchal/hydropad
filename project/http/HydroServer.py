import threading
from project.Config import Config
from aiohttp import web, WSCloseCode
import asyncio
from project.Runtime import Runtime
from project.http.HydroHttp import HydroHttp
from threading import Thread

class HydroServer(Thread):
    def __init__(self):
        Thread.__init__(self)
        ## handler = Handler()
        self.app = web.Application()
        self.app.add_routes([
            web.get('/', self.handle_index),
            web.static('/web', 'web'),
            web.get('/ws', self.handle_websocket),
            web.post('/command', self.handle_post)
        ])

    def run(self):
        loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)

        self.runner = web.AppRunner(self.app, access_log=None)
        loop.run_until_complete(self.runner.setup())
        print(f'http://{Config.server_name()}:{Config.server_port()}/')

        # site = web.TCPSite(runner, Config.server_name(), Config.server_port())
        site = web.TCPSite(self.runner, Config.server_name(), Config.server_port())
        loop.run_until_complete(site.start())   
        loop.run_forever()
        # runner = web.AppRunner(self.app)
        
        # self.loop.run_until_complete(runner.setup())
        # site = web.TCPSite(runner, Config.server_name(), Config.server_port())
        # self.loop.run_until_complete(site.start())                



    # handle ,,index.html''
    async def handle_index(self, request):
        return web.Response(text=self.load_index(), content_type="text/html")

    # handle ,,index.html''
    async def handle_post(self, request):
        return web.Response(text="OK", content_type="text/html")

    # handle ws
    async def handle_websocket(self, request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        async for msg in ws:
            print(msg.data)
            split = msg.data.split('/')
            Runtime.handle_message_multiple(split)
            ws.send_str('ok')
            
            # if msg.type == aiohttp.WSMsgType.TEXT:
            #     if msg.data == 'close':
            #         await ws.close()
            #     else:
            #         await ws.send_str('some websocket message payload')
            # elif msg.type == aiohttp.WSMsgType.ERROR:
            #     print('ws connection closed with exception %s' % ws.exception())

        return ws

    def load_index(self):
        filePath = "web/index.html"
        f = open(filePath, "r")
        content = f.read()

        # TODO: do replace wss bootstrap
        return content


# import aiohttp
# from aiohttp import web, WSCloseCode
# import asyncio

# async def websocket_handler(request):
#     ws = web.WebSocketResponse()
#     await ws.prepare(request)

#     async for msg in ws:
#         if msg.type == aiohttp.WSMsgType.TEXT:
#             if msg.data == 'close':
#                 await ws.close()
#             else:
#                 await ws.send_str('some websocket message payload')
#         elif msg.type == aiohttp.WSMsgType.ERROR:
#             print('ws connection closed with exception %s' % ws.exception())

#     return ws





# def thread_function(loop):
#     try:
#         loop.run_forever()
#     except KeyboardInterrupt:
#         pass
#     # loop.
