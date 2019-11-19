import asyncio
import json
import logging
import websockets

class WebSocket(object) :

    async def register(self,websocket):
        self.Clients.append(websocket)


    async def majChat(self,message):
        mes=json.dumps({"contenu" : message})
        await asyncio.wait([client.send(mes) for client in self.Clients])

    async def ConnexionWebSocket(self,websocket, path):
        
        # register(websocket) sends user_event() to websocket
        await self.register(websocket)
        try:
            async for message in websocket:
                data = json.loads(message)
                await self.majChat(data["contenu"])

        finally:
            await self.unregister(websocket)


    def __init__(self):
        self.Clients=[]

        start_server = websockets.serve(self.ConnexionWebSocket, "localhost", 6790)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

test=WebSocket()

