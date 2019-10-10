import asyncio
import json
import logging
import websockets


Utilisateur=[]

async def register(websocket):
    print("coucou ")
    Utilisateur.append(websocket)
    print(len(Utilisateur))

async def majChat(message):
    mes=json.dumps({"type":"chat","contenu" : message})
    await asyncio.wait([utilisateur.send(mes) for utilisateur in Utilisateur])


async def unregister(websocket):
    Utilisateur.remove(websocket)

async def notifierUtilisateurs():
    mes=json.dumps({"type":"nbUtilisateurs","contenu" : str(len(Utilisateur))})
    await asyncio.wait([utilisateur.send(mes) for utilisateur in Utilisateur])

async def utilisateur(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    try:
        await notifierUtilisateurs()
        async for message in websocket:
            await majChat(message);
    finally:
        await unregister(websocket)





start_server = websockets.serve(utilisateur, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
