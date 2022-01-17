from project.Config import Config
from aiohttp import web, WSCloseCode
import asyncio
from project.Runtime import Runtime
from project.http.HydroHttp import HydroHttp
from threading import Thread

class HydroServer(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.app = web.Application()
        self.app.add_routes([
            web.get('/', self.handle_index),
            web.static('/web', 'web'),
            web.get('/ws', self.handle_websocket),
            web.post('/command', self.handle_post)  ## TODO: remove and/or as option
        ])

    # main handler entrypoint (thread/loop)
    def run(self):
        loop = asyncio.new_event_loop()

        runner = web.AppRunner(self.app, access_log=None)
        loop.run_until_complete(runner.setup())
        print(f'http://{Runtime.get_server_ip()}/')

        site = web.TCPSite(runner, Config.server_name(), Config.server_port())
        loop.run_until_complete(site.start())   
        loop.run_forever()

    # handle ,,index.html''
    async def handle_index(self, request):
        return web.Response(text=self.load_index(), content_type="text/html")

    # handle command
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
        f.close()
        return content.replace("{hydropad:WS_ADDRESS}", f"ws://{Runtime.get_server_ip()}/ws")

