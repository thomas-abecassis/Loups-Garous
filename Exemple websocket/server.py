import asyncio
import json
import logging
import websockets

class WebSocket(object) :


    def register(self,websocket):
        self.Clients.append(websocket)

    def unregister(self,websocket):
        self.Clients.remove(websocket)

    async def majChat(self,message):
        mes=json.dumps({"contenu" : message}) ## on créer un json
        await asyncio.wait([client.send(mes) for client in self.Clients])
        ## qu'on envoie à nos clients

    async def ConnexionWebSocket(self,websocket, path):
        ## les attributs websocket et path sont donnés automatiquement par la bibliothèque
        
        self.register(websocket) ## l'objet websocket nous sert à faire la connexion avec un client, c'est avec cet objet 
        				    ## que l'on recoit(for message in websocket) et envoie(send) des informations
        try:
            async for message in websocket: ## a chaque fois qu'un message est reçu ce code est executé
                data = json.loads(message)
                ## le script js nous envoie un json, c'est avec json.loads que l'on "charge" le json
                await self.majChat(data["contenu"])

        finally:
            self.unregister(websocket)
            ## quand le client se déconnecte de la page on prend soint de l'enlever de la liste de client


    def __init__(self):
        self.Clients=[]
        ## on initialise la liste où on va stocker les clients qui se connecte

        start_server = websockets.serve(self.ConnexionWebSocket, "localhost", 7296)
        ## on lance le serveur, cette fonction prend en parametre :
        ## une fonction à lancer, l'adresse sur laquelle heberger la connexion et le numéro de port

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

test=WebSocket() ## on créer le websocket (sans cette ligne ca ne marchera pas)
