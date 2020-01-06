import asyncio
import json
import logging
import websockets
import partie as p
import intCons as IC
import intWeb as IW
import time
import client as cl

class WebSocket(object) :


    async def register(self,websocket):
        print(len(self.Utilisateur))
        if(len(self.joueur)>0):
            client=cl.Client(self.joueur[0],websocket)
            self.Utilisateur.append(client)
            self.joueur.pop(0)
        else :
            mes=json.dumps({"type":"chat","contenu" : "désolé tu ne peux pas jouer car la partie est remplie"})
            await websocket.send(mes)

    async def majChat(self,message,ws):
        client=self.clientAvecWebsocket(ws)
        self.chat.append([message,client])

        message=client.getNom()+ " >> " +message
        mes=json.dumps({"type":"chat","contenu" : message})
        await asyncio.wait([utilisateur.envoyerMessage(mes) for utilisateur in self.Utilisateur])

    async def majChatLG(self,message,ws):
        client=self.clientAvecWebsocket(ws)
        self.chat.append([message,client])

        message=client.getNom() + " >> " + message
        mes=json.dumps({"type":"chat","contenu" : message})
        for utilisateur in self.Utilisateur:
            if (utilisateur.estLoupGarou()):
                await utilisateur.envoyerMessage(mes)

    async def majChatLGPartie(self,message):
        mes=json.dumps({"type":"chat","contenu" : message})
        for utilisateur in self.Utilisateur:
            if (utilisateur.estLoupGarou()):
                await utilisateur.envoyerMessage(mes)

    async def majChatPartie(self,message):
        mes=json.dumps({"type":"chat","contenu" : message})
        for utilisateur in self.Utilisateur:
            await utilisateur.envoyerMessage(mes)

    async def majChatUnRole(self, message, role):
        utilisateur=self.clientAvecRole(role)
        if(utilisateur==False):
            return
        mes=json.dumps({"type":"chat","contenu" : message})
        await utilisateur.envoyerMessage(mes)

    async def majChatUnJoueur(self, message, joueur):
        utilisateur=self.clientAvecJoueur(joueur)
        if(utilisateur==False):
            return
        mes=json.dumps({"type":"chat","contenu" : message})
        await utilisateur.envoyerMessage(mes)

    async def unregister(self,websocket):
        for utilisateur in self.Utilisateur:
            if utilisateur.memeWs(websocket):
                self.Utilisateur.remove(utilisateur)
                self.joueur.append(utilisateur.joueur)

    async def notifierUtilisateurs(self,cl):
        if(cl==False):
            return;
        mes=json.dumps({"type":"utilisateur","contenu" :"Bonjour "+ cl.joueur.nom +" vous êtes "+cl.joueur.role.devoile() })
        await cl.envoyerMessage(mes)

    async def majEtat(self,listeEtat):
        mes=json.dumps({"type":"etatPartie","contenu" : {"jour" : self.partie.getJour(), "joueurs" : listeEtat}})
        await asyncio.wait([utilisateur.envoyerMessage(mes) for utilisateur in self.Utilisateur])

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
            await asyncio.wait([utilisateur.envoyerMessage(mes) for utilisateur in self.Utilisateur])        
        
        
    async def recoieData(self,websocket, path):
        
        if(not self.partieCree):
            self.partieCree=True
            self.interface = IW.IntWeb(self)
            self.joueur = ["Remi", "Thomas", "Samuel", "Hugo", "Chollet", "Arnaud"]
            self.roles = ["LG", "SV", "Voyante", "LG" , "SV", "Chasseur"]
            self.partie = p.Partie(self.interface, self.joueur, self.roles.copy())
            if(not self.partieLancee):
                loop = asyncio.get_event_loop()
                loop.create_task(self.partie.playGame())
                self.partieLancee=True 
                self.joueur=self.partie.playerbase.copy()
                print("Partie Créée ! et lancée !")


        
        # register(websocket) sends user_event() to websocket
        await self.register(websocket)
        try:
            await self.notifierUtilisateurs(self.clientAvecWebsocket(websocket))
            await self.partie.interface.mettreAJour(self.partie)
            async for message in websocket:
                data = json.loads(message)
                if data["type"]=="chat":
                    data["contenu"]=data["contenu"].replace('<','')
                    if(self.partie.getJour()):
                        await self.majChat(data["contenu"],websocket)
                    else :
                        if(self.clientAvecWebsocket(websocket).estLoupGarou()):
                            await self.majChatLG(data["contenu"],websocket)
                elif data["type"]=="vote":
                    self.votes.append([data["contenu"],self.clientAvecWebsocket(websocket)])
                elif data["type"]=="jeu":
                    await self.jeu(websocket,int(data["contenu"])) 
        finally:
            await self.unregister(websocket)

    def getChat(self):
        return self.chat

    async def getChoix(self,votant):
        while(len(self.votes)==0):
            await asyncio.sleep(0.5)
        while (not self.votes[len(self.votes)-1][1].joueur in votant):
            await asyncio.sleep(0.5)
        if(self.votes[len(self.votes)-1][0]!="a"):
            temp=self.votes[len(self.votes)-1][0]
            mes=json.dumps({"type":"chat","contenu" : "tu as voté contre "+ self.partie.alive[self.votes[len(self.votes)-1][0]].nom})
            await self.votes[len(self.votes)-1][1].envoyerMessage(mes);
            self.votes[len(self.votes)-1][0]="a"
            votant.remove(self.votes[len(self.votes)-1][1].joueur)
            return temp




    def __init__(self):
        self.roles=["LG", "SV", "Voyante", "LG" , "SV", "Chasseur"]
        self.chat=[]
        self.Utilisateur=[]
        self.tour=0
        self.compteur=0
        self.partieCree=False
        self.partieLancee=False
        self.interface = []
        self.joueur = []
        self.partie = []
        self.votes = []
        start_server = websockets.serve(self.recoieData,"localhost", 6789)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    def clientAvecWebsocket(self,ws):
        for utilisateur in self.Utilisateur:
            if utilisateur.memeWs(ws):
                return utilisateur
        return False


    def clientAvecRole(self,role):
        for utilisateur in self.Utilisateur:
            if (utilisateur.memeRole(role)):
                return utilisateur
        return False

    def clientAvecJoueur(self,joueur):
        for utilisateur in self.Utilisateur:
            if (utilisateur.memeJoueur(joueur)):
                return utilisateur
        return False

def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False



test=WebSocket()
