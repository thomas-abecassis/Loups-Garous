import asyncio
import json
import logging
import websockets
import partie as p
import intCons as IC
import intWeb as IW
import time

class WebSocket(object) :


    async def register(self,websocket):
        self.Utilisateur.append(websocket)
        print(len(self.Utilisateur))

    async def majChat(self,message):
        if(not self.partieLancee):
            loop = asyncio.get_event_loop()
            loop.create_task(self.partie.playGame())
            self.partieLancee=True
        mes=json.dumps({"type":"chat","contenu" : message})
        await asyncio.wait([utilisateur.send(mes) for utilisateur in self.Utilisateur])

    async def unregister(self,websocket):
        global tour
        self.Utilisateur.remove(websocket)
        try :
            if(tour > self.Utilisateur.index(websocket)):
                tour-=1
        except :
            pass

    async def notifierUtilisateurs(self,):
        mes=json.dumps({"type":"nbUtilisateurs","contenu" : str(len(self.Utilisateur))})
        await asyncio.wait([utilisateur.send(mes) for utilisateur in self.Utilisateur])

    async def jeu(self,websocket,nb):
        global tour
        global compteur
        if(self.Utilisateur.index(websocket)==tour):
            compteur+=nb
            tour+=1;
            if(tour>=len(self.Utilisateur)):
                tour=0
            print("compteur = "+ str(compteur))
            print("c'est au tour de "+ str(tour+1))
            mes=json.dumps({"type":"jeu","contenu" : str(compteur)+ "C'est au tour de l'utilisateur numero " + str(tour)})
            await asyncio.wait([utilisateur.send(mes) for utilisateur in self.Utilisateur])        
        
        
    async def utilisateur(self,websocket, path):
        
        if(not self.partieCree):
            self.partieCree=True
            self.interface = IW.IntWeb(self)
            self.joueur = ["Remi", "Thomas", "Samuel", "Hugo", "Chollet", "Arnaud"]
            self.role = ["LG", "SV", "Voyante", "LG" , "SV", "Chasseur"]
            self.partie = p.Partie(self.interface, self.joueur, self.role)
            print("Partie Créée !")


        
        # register(websocket) sends user_event() to websocket
        await self.register(websocket)
        try:
            await self.notifierUtilisateurs()
            async for message in websocket:
                data = json.loads(message)
                if data["type"]=="chat":
                    await self.majChat(data["contenu"])
                    self.chat.append(data["contenu"])
                    print(self.chat)
                elif data["type"]=="jeu":
                    await self.jeu(websocket,int(data["contenu"]))
        finally:
            await self.unregister(websocket)

    def getChat(self):
        return self.chat

    async def getChoix(self):
        while (not representsInt(self.chat[len(self.chat)-1])):
            await asyncio.sleep(0.5)
        temp=self.chat[len(self.chat)-1]
        self.chat[len(self.chat)-1]="a"
        return temp


    def __init__(self):
        self.chat=[]
        self.Utilisateur=[]
        self.tour=0
        self.compteur=0
        self.partieCree=False
        self.partieLancee=False
        self.interface = []
        self.joueur = []
        self.role = []
        self.partie = []
        start_server = websockets.serve(self.utilisateur, "localhost", 6789)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

test=WebSocket()
