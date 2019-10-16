
import asyncio
import websockets

async def ER(websocket, path):

    nom = await websocket.recv()
    coucou = "coucou {nom }"
    await websocket.send(coucou)





start_server = websockets.serve(ER, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

print("coucou")
