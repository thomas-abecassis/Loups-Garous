import asyncio
import json
import logging
import websockets
##Le mot clé async permet de marquer une fonction comme étant une coroutine asynchrone
##Clients.index(WebSocket)


class WebSocket(object) :

    def __init__(self):
        self.Clients=[] ## on initialise la liste où on va stocker les clients qui se connecte

        start_server = websockets.serve(self.ConnexionWebSocket, "localhost", 6790) ## on lance le serveur, cette fonction prend en parametre :
        																			## une fonction à lancer, l'adresse sur laquelle heberger la connexion et le numéro de port

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    def register(self,websocket): #Crée un nouveau client
        self.Clients.append(websocket)

    def unregister(self,websocket): #Supprime un nouveau client
        self.Clients.remove(websocket)

    async def ConnexionWebSocket(self,websocket, path): ## les attributs websocket et path sont donnés automatiquement par la bibliothèque
            
            self.register(websocket) ## l'objet websocket nous sert à faire la connexion avec un client, c'est avec cet objet 
                                        ## que l'on recoit(for message in websocket) et envoie(send) des informations
            try:
                async for message in websocket:
                    data = json.loads(message) ## le script js nous envoie un json, c'est avec json.loads que l'on "charge" le json
                    await self.majChat(data["contenu"])

            finally:
                self.unregister(websocket) ## quand le client se déconnecte de la page on prend soint de l'enlever de la liste de client

    async def majChat(self,message):
        print("compteur = "+ Clients.index(webSocket))
        mes=json.dumps({"contenu" : message}) ## on créer un json
        await asyncio.wait([client.send(mes) for client in self.Clients]) ##att que le message soit envoyé à tout le monde (qu'on envoie à nos clients)

      
test=WebSocket() ## on créer le websocket (sans cette ligne ca ne marchera pas)
