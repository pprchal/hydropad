from multiprocessing import Condition

import aiohttp
from project.Config import Config
from aiohttp import web, WSCloseCode
import asyncio
from project.Runtime import Runtime
from threading import Thread
from project.Queue import Queue

class HydroServerPush(Thread):
    def __init__(self, ws):
        Thread.__init__(self)
        self.ws = ws

    # push events to browser
    def run(self):
        loop = asyncio.new_event_loop()
        with Queue.cond:
            Queue.cond.wait()
            if self.ws.closed:
                return

            while len(Queue.queue) >= 1:
                message = Queue.queue.pop()

                # stop if connection died
                if message == "close" :
                    return
                loop.run_until_complete(self.ws.send_str(message))
            

class HydroServer(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.app = web.Application()
        self.app.add_routes([
            web.get('/', self.handle_index),
            web.static('/web', 'web'),
            web.get('/ws', self.handle_websocket)
        ])
        self.client_id = 0

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
        return web.Response(text=self.load_content(request), content_type="text/html")


    # handle ws
    async def handle_websocket(self, request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        # start push thread
        push_thread = HydroServerPush(ws)
        push_thread.start()
        self.client_id = self.client_id + 1
        print(f"websocket connected {request.url} - assigned client_id: {self.client_id}")
        await ws.send_str(f"client_id: {self.client_id}")

        async for msg in ws:
            print(msg.data)
            split = msg.data.split('/')
            Runtime.handle_message_multiple(split)
            
            if msg.type == aiohttp.WSMsgType.TEXT:
                if msg.data == 'close':
                    Queue.queue_message('close')
                    await ws.close()
                else:
                    await ws.send_str('some websocket message payload')
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print('ws connection closed with exception %s' % ws.exception())

        return ws

    # load index.html, replace vars
    def load_content(self, request):
        filePath = "web/index.html"
        f = open(filePath, "r")
        content = f.read()
        f.close()
        return content.replace("{hydropad:WS_ADDRESS}", f"ws://{Runtime.get_server_ip()}/ws")
