import asyncio

class IntWeb(object):
    """docstring for IntWeb."""
    def __init__(self,ws):
        self.webSocket=ws
        super(IntWeb, self).__init__()

    async def afficher(self, message):
        await self.webSocket.majChatPartie(message)

    async def afficherAUnJoueur(self,message,joueur):
        await self.webSocket.majChatUnJoueur(message,joueur)

    async def afficherAUnRole(self,message,role):
        await self.webSocket.majChatUnRole(message,role)

    async def afficherPourLeslg(self,message):
        await self.webSocket.majChatLGPartie(message)

    async def mettreAJour(self, partie):
        partie.updateGame()
        await self.webSocket.majEtat(getEtatsJoueurs(partie))

    async def faireChoix(self, list,votant):
        choix=await self.webSocket.getChoix(votant)
        print("je fais un choix")
        try :
            choix = int(choix)
        except :
            choix=-1
        while (choix >= len(list) or choix < 0):
            choix=await self.webSocket.getChoix(votant)
            try :
                choix = int(choix)
            except :
                choix =-1
            await asyncio.sleep(0.5)
        choix = list[choix]
        return (choix)

    async def faireVote(self, partie, votant, list):
        votant=votant.copy()
        vote = []
        for i in range (len(votant)):
            vote.append(await self.faireChoix(list,votant))
        vote =  partie.majorite(vote)
        return (vote)





def getEtatsJoueurs(partie):
    village=partie.playerbase
    l=[]
    for player in village : 
        if (player.vivant):
            l.append([player.nom,True])
        else :
            l.append([player.nom,False])
    return l