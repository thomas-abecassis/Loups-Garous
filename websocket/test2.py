import asyncio
import json
import logging
import websockets


Utilisateur=[]
tour=0
compteur=0

async def register(websocket):
    Utilisateur.append(websocket)
    print(len(Utilisateur))

async def majChat(message):
    mes=json.dumps({"type":"chat","contenu" : message})
    await asyncio.wait([utilisateur.send(mes) for utilisateur in Utilisateur])


async def unregister(websocket):
    global tour
    Utilisateur.remove(websocket)
    try :
        if(tour > Utilisateur.index(websocket)):
            tour-=1
    except :
        pass

async def notifierUtilisateurs():
    mes=json.dumps({"type":"nbUtilisateurs","contenu" : str(len(Utilisateur))})
    await asyncio.wait([utilisateur.send(mes) for utilisateur in Utilisateur])

async def jeu(websocket,nb):
    global tour
    global compteur
    if(Utilisateur.index(websocket)==tour):
        compteur+=nb
        tour+=1;
        if(tour>=len(Utilisateur)):
            tour=0
        print("compteur = "+ str(compteur))
        print("c'est au tour de "+ str(tour+1))
        mes=json.dumps({"type":"jeu","contenu" : str(compteur)+ "C'est au tour de l'utilisateur numero " + str(tour)})
        await asyncio.wait([utilisateur.send(mes) for utilisateur in Utilisateur])        
    
    
async def utilisateur(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    try:
        await notifierUtilisateurs()
        async for message in websocket:
            data = json.loads(message)
            if data["type"]=="chat":
                await majChat(data["contenu"])
            elif data["type"]=="jeu":
                await jeu(websocket,int(data["contenu"]))
    finally:
        await unregister(websocket)





start_server = websockets.serve(utilisateur, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
