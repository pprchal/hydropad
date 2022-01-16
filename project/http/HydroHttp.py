from project.Runtime import Runtime
from aiohttp import web, WSCloseCode

class HydroHttp(web.View):
    # dispatch commands from mobile
    async def post(self):
        # c/play/[volume]
        # n/note
        data = await self.request.content.read()
        string = data.decode('utf8')
        print(string)
        ## Runtime.handle_message_multiple(string.split('/'))
        return web.Response(text="", status=200)
